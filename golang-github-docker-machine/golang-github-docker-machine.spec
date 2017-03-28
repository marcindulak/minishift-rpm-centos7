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
# FAIL	github.com/docker/machine/cmd [build failed]
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
%global project         docker
%global repo            machine
# https://github.com/docker/machine
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          93b7ba6171d5d0fe89279e8651c606df9975f9e5
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.10.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Machine management for a container-centric world
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{version}.tar.gz

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
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/compute)  # missing
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/network)  # missing
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/resources/resources)  # missing
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/resources/subscriptions)  # missing
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/storage)  # missing
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/Azure/go-autorest/autorest)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/to)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/bugsnag/bugsnag-go)
BuildRequires: golang(github.com/codegangsta/cli)
BuildRequires: golang(github.com/digitalocean/godo)
BuildRequires: golang(github.com/docker/docker/pkg/term)
BuildRequires: golang(github.com/pyr/egoscale/src/egoscale)
BuildRequires: golang(github.com/rackspace/gophercloud)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/floatingip)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/keypairs)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/startstop)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/flavors)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/images)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/compute/v2/servers)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/identity/v2/tenants)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/networking/v2/extensions/layer3/floatingips)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/networking/v2/networks)
BuildRequires: golang(github.com/rackspace/gophercloud/openstack/networking/v2/ports)
BuildRequires: golang(github.com/rackspace/gophercloud/pagination)
BuildRequires: golang(github.com/rackspace/gophercloud/rackspace)
BuildRequires: golang(github.com/samalba/dockerclient)
BuildRequires: golang(github.com/skarademir/naturalsort)
BuildRequires: golang(github.com/vmware/govcloudair)
BuildRequires: golang(github.com/vmware/govmomi)
BuildRequires: golang(github.com/vmware/govmomi/find)
BuildRequires: golang(github.com/vmware/govmomi/guest)
BuildRequires: golang(github.com/vmware/govmomi/object)
BuildRequires: golang(github.com/vmware/govmomi/vim25/mo)
BuildRequires: golang(github.com/vmware/govmomi/vim25/soap)
BuildRequires: golang(github.com/vmware/govmomi/vim25/types)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/windows/registry)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
%endif

Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/compute)
Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/network)
Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/resources/resources)
Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/resources/subscriptions)
Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/storage)
Requires:      golang(github.com/Azure/azure-sdk-for-go/storage)
Requires:      golang(github.com/Azure/go-autorest/autorest)
Requires:      golang(github.com/Azure/go-autorest/autorest/azure)
Requires:      golang(github.com/Azure/go-autorest/autorest/to)
Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/aws/awserr)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/aws/aws-sdk-go/service/ec2)
Requires:      golang(github.com/bugsnag/bugsnag-go)
Requires:      golang(github.com/codegangsta/cli)
Requires:      golang(github.com/digitalocean/godo)
Requires:      golang(github.com/docker/docker/pkg/term)
Requires:      golang(github.com/pyr/egoscale/src/egoscale)
Requires:      golang(github.com/rackspace/gophercloud)
Requires:      golang(github.com/rackspace/gophercloud/openstack)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/floatingip)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/keypairs)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/extensions/startstop)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/flavors)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/images)
Requires:      golang(github.com/rackspace/gophercloud/openstack/compute/v2/servers)
Requires:      golang(github.com/rackspace/gophercloud/openstack/identity/v2/tenants)
Requires:      golang(github.com/rackspace/gophercloud/openstack/networking/v2/extensions/layer3/floatingips)
Requires:      golang(github.com/rackspace/gophercloud/openstack/networking/v2/networks)
Requires:      golang(github.com/rackspace/gophercloud/openstack/networking/v2/ports)
Requires:      golang(github.com/rackspace/gophercloud/pagination)
Requires:      golang(github.com/rackspace/gophercloud/rackspace)
Requires:      golang(github.com/samalba/dockerclient)
Requires:      golang(github.com/skarademir/naturalsort)
Requires:      golang(github.com/vmware/govcloudair)
Requires:      golang(github.com/vmware/govmomi)
Requires:      golang(github.com/vmware/govmomi/find)
Requires:      golang(github.com/vmware/govmomi/guest)
Requires:      golang(github.com/vmware/govmomi/object)
Requires:      golang(github.com/vmware/govmomi/vim25/mo)
Requires:      golang(github.com/vmware/govmomi/vim25/soap)
Requires:      golang(github.com/vmware/govmomi/vim25/types)
Requires:      golang(golang.org/x/crypto/ssh)
Requires:      golang(golang.org/x/crypto/ssh/terminal)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/sys/windows/registry)
Requires:      golang(google.golang.org/api/compute/v1)
Requires:      golang(google.golang.org/api/googleapi)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/commands) = %{version}-%{release}
Provides:      golang(%{import_path}/commands/commandstest) = %{version}-%{release}
Provides:      golang(%{import_path}/commands/mcndirs) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/amazonec2) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/azure) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/azure/azureutil) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/azure/logutil) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/digitalocean) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/driverutil) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/errdriver) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/exoscale) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/fakedriver) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/generic) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/google) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/hyperv) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/none) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/openstack) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/rackspace) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/softlayer) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/virtualbox) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/vmwarefusion) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/vmwarevcloudair) = %{version}-%{release}
Provides:      golang(%{import_path}/drivers/vmwarevsphere) = %{version}-%{release}
Provides:      golang(%{import_path}/its) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/auth) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/cert) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/check) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/crashreport) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/drivers) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/drivers/plugin) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/drivers/plugin/localbinary) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/drivers/rpc) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/engine) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/host) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/hosttest) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/libmachinetest) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/log) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/mcndockerclient) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/mcnerror) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/mcnflag) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/mcnutils) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/persist) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/persist/persisttest) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/provider) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/provision) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/provision/pkgaction) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/provision/provisiontest) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/provision/serviceaction) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/shell) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/ssh) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/ssh/sshtest) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/state) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/swarm) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/version) = %{version}-%{release}
Provides:      golang(%{import_path}/libmachine/versioncmp) = %{version}-%{release}
Provides:      golang(%{import_path}/version) = %{version}-%{release}

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
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/stretchr/testify/mock)
%endif

Requires:      golang(github.com/stretchr/testify/assert)
Requires:      golang(github.com/stretchr/testify/mock)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{version}

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

%gotest %{import_path}/cmd
%gotest %{import_path}/commands
%gotest %{import_path}/commands/mcndirs
%gotest %{import_path}/drivers/amazonec2
%gotest %{import_path}/drivers/azure
%gotest %{import_path}/drivers/digitalocean
%gotest %{import_path}/drivers/driverutil
%gotest %{import_path}/drivers/exoscale
%gotest %{import_path}/drivers/generic
%gotest %{import_path}/drivers/google
%gotest %{import_path}/drivers/hyperv
%gotest %{import_path}/drivers/openstack
%gotest %{import_path}/drivers/rackspace
%gotest %{import_path}/drivers/softlayer
%gotest %{import_path}/drivers/virtualbox
%gotest %{import_path}/drivers/vmwarefusion
%gotest %{import_path}/drivers/vmwarevcloudair
%gotest %{import_path}/drivers/vmwarevsphere
%gotest %{import_path}/its/cli
%gotest %{import_path}/its/thirdparty
%gotest %{import_path}/libmachine/cert
%gotest %{import_path}/libmachine/check
%gotest %{import_path}/libmachine/crashreport
%gotest %{import_path}/libmachine/drivers
%gotest %{import_path}/libmachine/drivers/plugin/localbinary
%gotest %{import_path}/libmachine/drivers/rpc
%gotest %{import_path}/libmachine/host
%gotest %{import_path}/libmachine/log
%gotest %{import_path}/libmachine/mcnutils
%gotest %{import_path}/libmachine/persist
%gotest %{import_path}/libmachine/persist/persisttest
%gotest %{import_path}/libmachine/provision
%gotest %{import_path}/libmachine/provision/pkgaction
%gotest %{import_path}/libmachine/provision/provisiontest
%gotest %{import_path}/libmachine/provision/serviceaction
%gotest %{import_path}/libmachine/shell
%gotest %{import_path}/libmachine/ssh
%gotest %{import_path}/libmachine/state
%gotest %{import_path}/libmachine/versioncmp
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc ROADMAP.md README.md CONTRIBUTING.md CHANGELOG.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc ROADMAP.md README.md CONTRIBUTING.md CHANGELOG.md
%endif

%changelog
* Tue Mar 28 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.10.0-0.1.git93b7ba6
- First package for Fedora

