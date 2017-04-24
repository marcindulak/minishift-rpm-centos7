import yaml

stream = open('glide.yaml', 'r')
packages = yaml.load(stream)['import']

def gopackage(package, operator, version):
    return 'golang(' + package + ') ' + operator + ' ' + version

def bundled_dependency(package, version, bundled_source_number=0):
    provider_full, username, project = package.split('/')
    provider, provider_tld = provider_full.split('.')
    ret = ['Provides:           bundled({}) = {}'.format(package, version)]
    if len(version) == 40:  # test for sha1
        try:
            int(version, 16)
            commit = version
        except ValueError:
            commit = None
    else:
        commit = None
    if not commit is None:
        shortcommit = commit[:7]
        # https://github.com/blang/semver/archive/4a1e882c79dcf4ec00d2e29fac74b9c8938d5052.zip
        # https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
        url = 'Source{:02d}:           https://github.com/{}/{}/archive/{}/{}-{}.tar.gz'.format(
            bundled_source_number, username, project, commit, project, shortcommit)
    else:
        # https://github.com/blang/semver/archive/v3.5.0.tar.gz
        if version.startswith('v'):
            versiontag = version
        else:
            versiontag = 'v' + version
        url = 'Source{:02d}:           https://github.com/{}/{}/archive/{}.tar.gz'.format(
            bundled_source_number, username, project, versiontag)
    ret.append(url)
    return ret

# Any versioned golang package is considered a bundled dependency
bundled_source_number_start = 10  # Source0 is minishift itself
bundled_source_number = bundled_source_number_start
dependencies = []
for entry in packages:
    version = str(entry.get('version', ''))
    package = entry['package']
    package = package.strip('/')  # in case uri ends with /
    subpackages = []
    if 'subpackages' in entry:
        subpackages = [package + '/' + subpackage for subpackage in entry['subpackages']]
    else:
        subpackages = [package]
    if version == '':
        dependency = []
        for subpackage in subpackages:
            dependency.append('BuildRequires:      ' + 'golang(' + subpackage + ')')
    else:
        modifier = None
        # http://stackoverflow.com/questions/40168086/vendoring-golang-shared-repository
        if version[0] in ['^', '~']:
            modifier = version[0]
            version = version[1:]
        # http://semver.org/
        try:
            dummy = version.split('.')
            if len(version.split('.')) == 2:  # major.minor
                major, minor = version.split('.')
                patch = None
            elif len(version.split('.')) == 3:  # major.minor.patch
                major, minor, patch = version.split('.')
            else:
                dependency = []
                for subpackage in subpackages:
                    dependency.append(gopackage(subpackage, '=', version))
        except ValueError:  # a git hash or no dot in version
            dependency = []
            for subpackage in subpackages:
                dependency.append(gopackage(subpackage, '=', version))
        if modifier is None:
            dependency = []
            for subpackage in subpackages:
                dependency.append(gopackage(subpackage, '=', version))
        else:
            dependency = []
            for subpackage in subpackages:
                if modifier == '^':
                    if patch is None:
                        dependency.append(gopackage(subpackage, '>=', version) + ', ' +
                                          gopackage(subpackage, '<', str(int(major) + 1) + '.' + minor))
                    else:
                        dependency.append(gopackage(subpackage, '>=', version) + ', ' +
                                          gopackage(subpackage, '<', str(int(major) + 1) + '.' + minor + '.' + str(0)))
                elif modifier == '~':
                    if patch is None:
                        dependency.append(gopackage(subpackage, '>=', version) + ', ' +
                                          gopackage(subpackage, '<', major + '.' + str(int(minor) + 1)))
                    else:
                        dependency.append(gopackage(subpackage, '>=', version) + ', ' +
                                          gopackage(subpackage, '<', major + '.' + str(int(minor) + 1) + '.' + str(0)))
                else:
                    dependency = []
                    for subpackage in subpackages:
                        dependency.append(gopackage(package, '=', version))
        # handle bundled dependencies
        dependency = ['# {}'.format(package),
                      '%if ! 0%{?with_bundled}',
                      'BuildRequires:      ' + dependency[0],  # this is the root of the package
                      '%else']
        dependency.extend(bundled_dependency(package, version, bundled_source_number))
        dependency.append('%endif')
        bundled_source_number = bundled_source_number + 1
    dependencies.append(dependency)

if bundled_source_number > bundled_source_number_start:  # any dependencies got bundled?
    print('# Bundled dependencies sources')
    print('%global bundled_source_start {}'.format(bundled_source_number_start))
    print('%global bundled_source_end {}'.format(bundled_source_number - 1))
    print('\n')
    
for dependency in dependencies:
    for build_requires in dependency:
        print(build_requires)
    print('\n')
