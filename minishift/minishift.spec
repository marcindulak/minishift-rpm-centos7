%if 0%{?fedora}
%global with_devel 1
%global with_bundled 1
%global with_debug 1
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 1
%global with_unit_test 0
%endif


%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         minishift
%global repo            minishift
# https://github.com/minishift/minishift
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          cebec68fcf03ae5b5a9c0b808178b542c17215a7
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           %{repo}
Version:        1.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Run a single-node OpenShift cluster inside a VM
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        glide2specinc.inc
%include        %{SOURCE1}

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}


%prep
%setup -q -n %{repo}-%{commit}
# https://github.com/marcindulak/minishift-rpm-centos7/issues/5
for file in `find . -type f`;
do
    sed -i 's|gopkg.in/cheggaaa/pb.v1|github.com/cheggaaa/pb|' $file
done
# copy the sources
%global sources %{expand: %{lua: for i=10,18 do print("%{SOURCE"..i.."} ") end}}
for source in %{sources};
do
    cp -pv %{_sourcedir}/`basename $(echo ${source} | cut -d'#' -f2)` .
done


%build
mkdir vendor
pushd vendor
# untar
for tarball in ../*.tar.gz;
do
    tar zxf ${tarball}
done
# get rid of versions
for dir in *-*;
do
    mv -v ${dir} `echo ${dir} | rev | cut -d'-' -f2- | rev`
done

%global import_paths %{expand: %{lua: for i=10,18 do print("%{import_path_"..i.."} ") end}}
for import_path in %{import_paths};
do
    dir=`basename $(echo ${import_path})`
    pushd $dir
    #MDTMP TODO - need to build binaries for relevant packages here and install them
    rm -rf vendor  # don't bundle what bundled packages bundle
    install -d -p %{buildroot}/%{gopath}/src/${import_path}/
    echo "%%dir %%{gopath}/src/${import_path}/." >> ../bundled.file-list
    # find all *.go but no *_test.go files and generate bundled.file-list
    for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" -and -not -ipath "*vendor*") ; do
	dirprefix=$(dirname $file)
	install -d -p %{buildroot}/%{gopath}/src/${import_path}/$dirprefix
	cp -pav $file %{buildroot}/%{gopath}/src/${import_path}/$file
	echo "%%{gopath}/src/${import_path}/$file" >> ../bundled.file-list

        while [ "$dirprefix" != "." ]; do
            echo "%%dir %%{gopath}/src/${import_path}/$dirprefix" >> ../bundled.file-list
            dirprefix=$(dirname $dirprefix)
        done
    done
    popd
done
popd

# set up temporary build gopath, and put our directory there
mkdir build
cp -rp addons cmd pkg scripts test build
pushd build
export GOPATH=%{gopath}
export PATH="$PATH:$GOPATH/bin"
popd
make

%install

%post
%systemd_post %{repo}

%preun
%systemd_preun %{repo}

%postun
%systemd_postun_with_restart %{repo}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md 

%changelog
* Mon Apr 24 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.0.0-0.1.gitcebec68
- First package for Fedora
