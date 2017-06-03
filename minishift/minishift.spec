%if 0%{?fedora}
%global with_devel 1
%global with_bundled 1
%global with_debug 0
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
%global commit          270a4da8a68f96d93895e4aea3534efda868dd15
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
# https://github.com/minishift/minishift/issues/830
Patch0:         830.patch

BuildRequires:  go-bindata
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/spf13/afero)
# https://github.com/minishift/minishift/issues/827
# https://bugzilla.redhat.com/show_bug.cgi?id=1427336
%if (0%{?fedora} && 0%{?fedora} < 27) || (0%{?rhel} && 0%{?rhel} < 8)
BuildRequires:  golang(github.com/spf13/jWalterWeatherman)
%else
BuildRequires:  golang(github.com/spf13/jwalterweatherman)
%endif


# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}


%prep
%setup -q -n %{repo}-%{commit}
%patch0

# https://github.com/marcindulak/minishift-rpm-centos7/issues/5
for file in `find . -type f`;
do
    sed -i 's|gopkg.in/cheggaaa/pb.v1|github.com/cheggaaa/pb|' $file
done


# copy the sources
%global sources %{expand: %{lua: for i=10,14 do print("%{SOURCE"..i.."} ") end}}
for source in %{sources};
do
    cp -pv %{_sourcedir}/`basename $(echo ${source} | cut -d'#' -f2)` .
done
# untar the sources under the directory "bundled"
mkdir bundled
pushd bundled
for tarball in ../*.tar.gz;
do
    tar zxf ${tarball}
done
# get rid of versions
for dir in *-*;
do
    mv -v ${dir} `echo ${dir} | rev | cut -d'-' -f2- | rev`
done
popd

# https://github.com/minishift/minishift/issues/827
# https://bugzilla.redhat.com/show_bug.cgi?id=1427336
%if (0%{?fedora} && 0%{?fedora} < 27) || (0%{?rhel} && 0%{?rhel} < 8)
for file in `find . -type f`;
do
    sed -i 's|jwalterweatherman|jWalterWeatherman|' $file
done
%endif

# prepare GOPATH
mkdir -p ./{bin,pkg,src}
export GOPATH=`pwd`

# https://github.com/minishift/minishift/issues/829
# !!!MDTMP: A terrible hack - minishift/Makefile uses GOPATH for two purposes:
# 1. GOPATH pointing to to packages locations, 2. GOPATH in the destination path of minishift target binary
rm -rfv /usr/share/gocode/src/github.com/minishift
pushd src
for dir in `find /usr/share/gocode/src -maxdepth 1 -mindepth 1 -type d`;
do
    ln -s $dir
done
popd

mkdir -p src/%{provider_prefix}
shopt -s extglob
mv -f !(src) src/%{provider_prefix}
pushd $GOPATH/src/%{provider_prefix}
# install budled packages under vendor directory
mkdir -v vendor
export VENDOR=$GOPATH/src/%{provider_prefix}/vendor
pushd bundled
%global import_paths %{expand: %{lua: for i=10,14 do print("%{import_path_"..i.."} ") end}}
for import_path in %{import_paths};
do
    dir=`basename $(echo ${import_path})`
    pushd $dir
    rm -rf bundled  # don't bundle what bundled packages bundle
    install -d -p $VENDOR/${import_path}/
    echo "%%dir %%{gopath}/src/${import_path}/." >> ../bundled.file-list
    # find all *.go but no *_test.go files and generate bundled.file-list
    for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" -and -not -ipath "*vendor*") ; do
	dirprefix=$(dirname $file)
	install -d -p $VENDOR/${import_path}/$dirprefix
	cp -pav $file $VENDOR/${import_path}/$file
	echo "%%{gopath}/src/${import_path}/$file" >> ../bundled.file-list

        while [ "$dirprefix" != "." ]; do
            echo "%%dir %%{gopath}/src/${import_path}/$dirprefix" >> ../bundled.file-list
            dirprefix=$(dirname $dirprefix)
        done
    done
    popd
done
popd

%build
export GOPATH=`pwd`
cd src/%{provider_prefix}
# we know test fail
GO_BINDATA=/usr/bin/go-bindata make
! GO_BINDATA=/usr/bin/go-bindata make test


%install
install -d -p %{buildroot}%{_bindir}
install -p -m 755 bin/%{project} %{buildroot}%{_bindir}


%check
%if 0%{?with_check}
export GOPATH=`pwd`
go test -v %{provider_prefix}
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%{_bindir}/%{project}
%license src/%{provider_prefix}/LICENSE
%doc src/%{provider_prefix}/README.adoc


%changelog
* Sat May 13 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.0.0-0.1.git270a4da
- First package for Fedora
