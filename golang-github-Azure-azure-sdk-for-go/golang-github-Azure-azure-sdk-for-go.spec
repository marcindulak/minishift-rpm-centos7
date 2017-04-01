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
# FAIL: authorization_test.go:190: AuthorizationSuite.Test_allSharedKeys
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
%global project         Azure
%global repo            azure-sdk-for-go
# https://github.com/Azure/azure-sdk-for-go
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          4897648e310020dae650a89c31ff633284c13a24
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        8.1.1
Release:        beta.1.git%{shortcommit}%{?dist}
Summary:        Microsoft Azure SDK for Go
# Detected licences
# - *No copyright* Apache (v2.0) at 'LICENSE'
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
BuildRequires: golang(github.com/Azure/go-autorest/autorest)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/date)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/to)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/validation)
BuildRequires: golang(github.com/satori/uuid)
BuildRequires: golang(github.com/shopspring/decimal)
BuildRequires: golang(golang.org/x/crypto/pkcs12)
%endif

Requires:      golang(github.com/Azure/go-autorest/autorest)
Requires:      golang(github.com/Azure/go-autorest/autorest/azure)
Requires:      golang(github.com/Azure/go-autorest/autorest/date)
Requires:      golang(github.com/Azure/go-autorest/autorest/to)
Requires:      golang(github.com/Azure/go-autorest/autorest/validation)
Requires:      golang(github.com/satori/uuid)
Requires:      golang(github.com/shopspring/decimal)
Requires:      golang(golang.org/x/crypto/pkcs12)

Provides:      golang(%{import_path}/arm/analysisservices) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/apimanagement) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/apimdeployment) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/authorization) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/batch) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/billing) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/cdn) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/cognitiveservices) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/commerce) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/compute) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/containerregistry) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/containerservice) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/customer-insights) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/datalake-analytics/account) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/datalake-store/account) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/devtestlabs) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/disk) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/dns) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/documentdb) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/eventhub) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/examples/helpers) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/graphrbac) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/intune) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/iothub) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/keyvault) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/logic) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/machinelearning/commitmentplans) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/machinelearning/webservices) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/mediaservices) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/mobileengagement) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/network) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/networkwatcher) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/notificationhubs) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/operationalinsights) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/powerbiembedded) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/recoveryservices) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/redis) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/features) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/links) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/locks) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/policy) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/resources) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/resources/subscriptions) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/scheduler) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/search) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/servermanagement) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/service-map) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/servicebus) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/sql) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/storage) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/storageimportexport) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/trafficmanager) = %{version}-%{release}
Provides:      golang(%{import_path}/arm/web) = %{version}-%{release}
Provides:      golang(%{import_path}/datalake-store/filesystem) = %{version}-%{release}
Provides:      golang(%{import_path}/dataplane/keyvault) = %{version}-%{release}
Provides:      golang(%{import_path}/management) = %{version}-%{release}
Provides:      golang(%{import_path}/management/affinitygroup) = %{version}-%{release}
Provides:      golang(%{import_path}/management/hostedservice) = %{version}-%{release}
Provides:      golang(%{import_path}/management/location) = %{version}-%{release}
Provides:      golang(%{import_path}/management/networksecuritygroup) = %{version}-%{release}
Provides:      golang(%{import_path}/management/osimage) = %{version}-%{release}
Provides:      golang(%{import_path}/management/sql) = %{version}-%{release}
Provides:      golang(%{import_path}/management/storageservice) = %{version}-%{release}
Provides:      golang(%{import_path}/management/testutils) = %{version}-%{release}
Provides:      golang(%{import_path}/management/virtualmachine) = %{version}-%{release}
Provides:      golang(%{import_path}/management/virtualmachinedisk) = %{version}-%{release}
Provides:      golang(%{import_path}/management/virtualmachineimage) = %{version}-%{release}
Provides:      golang(%{import_path}/management/virtualnetwork) = %{version}-%{release}
Provides:      golang(%{import_path}/management/vmutils) = %{version}-%{release}
Provides:      golang(%{import_path}/storage) = %{version}-%{release}

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
BuildRequires: golang(gopkg.in/check.v1)
%endif

Requires:      golang(gopkg.in/check.v1)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{version}-beta

%build
%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
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
for file in $(find . -iname "*_test.go") ; do
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
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/management
%gotest %{import_path}/management/storageservice
%gotest %{import_path}/management/virtualmachine
%gotest %{import_path}/management/virtualmachineimage
%gotest %{import_path}/management/vmutils
%gotest %{import_path}/storage
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md
%endif

%changelog
* Tue Mar 28 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 8.1.0-beta.1.git4897648
- First package for Fedora

