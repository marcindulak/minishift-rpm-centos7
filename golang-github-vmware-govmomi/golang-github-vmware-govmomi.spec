# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
# panic: open fixtures/system_hostname_get.xml: no such file or directory
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         vmware
%global repo            govmomi
# https://github.com/vmware/govmomi
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          f2b5f4d22362f9de1deac5bcd8ac4d1015cc5b3d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.13.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go library for the VMware vSphere API
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}



%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/davecgh/go-spew/spew)
%endif

Requires:      golang(github.com/davecgh/go-spew/spew)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/event) = %{version}-%{release}
Provides:      golang(%{import_path}/find) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/about) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/cli) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/cluster) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/datacenter) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/datastore) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/datastore/disk) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/datastore/vsan) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device/cdrom) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device/floppy) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device/scsi) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device/serial) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/device/usb) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/dvs) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/dvs/portgroup) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/env) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/events) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/extension) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/fields) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/flags) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/folder) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/account) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/autostart) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/cert) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/date) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/esxcli) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/firewall) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/maintenance) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/option) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/portgroup) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/service) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/storage) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/vnic) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/host/vswitch) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/importx) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/license) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/logs) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/ls) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/metric/interval) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/object) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/permissions) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/pool) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/role) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/session) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vapp) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/version) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm/disk) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm/guest) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm/network) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm/rdm) = %{version}-%{release}
Provides:      golang(%{import_path}/govc/vm/snapshot) = %{version}-%{release}
Provides:      golang(%{import_path}/guest) = %{version}-%{release}
Provides:      golang(%{import_path}/license) = %{version}-%{release}
Provides:      golang(%{import_path}/list) = %{version}-%{release}
Provides:      golang(%{import_path}/object) = %{version}-%{release}
Provides:      golang(%{import_path}/ovf) = %{version}-%{release}
Provides:      golang(%{import_path}/performance) = %{version}-%{release}
Provides:      golang(%{import_path}/property) = %{version}-%{release}
Provides:      golang(%{import_path}/session) = %{version}-%{release}
Provides:      golang(%{import_path}/task) = %{version}-%{release}
Provides:      golang(%{import_path}/test) = %{version}-%{release}
Provides:      golang(%{import_path}/test/functional) = %{version}-%{release}
Provides:      golang(%{import_path}/units) = %{version}-%{release}
Provides:      golang(%{import_path}/view) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/debug) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/methods) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/mo) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/progress) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/soap) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/types) = %{version}-%{release}
Provides:      golang(%{import_path}/vim25/xml) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif


%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%gotest %{import_path}/govc
%gotest %{import_path}/govc/flags
%gotest %{import_path}/govc/host/esxcli
%gotest %{import_path}/list
%gotest %{import_path}/object
%gotest %{import_path}/ovf
%gotest %{import_path}/session
%gotest %{import_path}/task
%gotest %{import_path}/test/functional
%gotest %{import_path}/units
%gotest %{import_path}/vim25
%gotest %{import_path}/vim25/methods
%gotest %{import_path}/vim25/mo
%gotest %{import_path}/vim25/progress
%gotest %{import_path}/vim25/soap
%gotest %{import_path}/vim25/types
%gotest %{import_path}/vim25/xml
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md CONTRIBUTORS CONTRIBUTING.md CHANGELOG.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE.txt
%doc README.md CONTRIBUTORS CONTRIBUTING.md CHANGELOG.md
%endif

%changelog
* Tue Mar 28 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.13.0-0.1.gitf2b5f4d
- First package for Fedora

