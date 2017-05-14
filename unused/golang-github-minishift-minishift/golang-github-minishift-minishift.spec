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
# minishift/pkg/minikube/cluster/cluster.go:44:2: cannot find package "gopkg.in/cheggaaa/pb.v1"
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

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
%global commit          e05dbec97583e9e15ec5aa6bc183f5b74288ff57
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Run a single-node OpenShift cluster inside a VM
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
BuildRequires: golang(github.com/asaskevich/govalidator)
BuildRequires: golang(github.com/blang/semver)
BuildRequires: golang(github.com/docker/go-units)
BuildRequires: golang(github.com/docker/machine/drivers/hyperv)
BuildRequires: golang(github.com/docker/machine/drivers/virtualbox)
BuildRequires: golang(github.com/docker/machine/drivers/vmwarefusion)
BuildRequires: golang(github.com/docker/machine/libmachine)
BuildRequires: golang(github.com/docker/machine/libmachine/auth)
BuildRequires: golang(github.com/docker/machine/libmachine/drivers)
BuildRequires: golang(github.com/docker/machine/libmachine/drivers/plugin)
BuildRequires: golang(github.com/docker/machine/libmachine/drivers/plugin/localbinary)
BuildRequires: golang(github.com/docker/machine/libmachine/engine)
BuildRequires: golang(github.com/docker/machine/libmachine/host)
BuildRequires: golang(github.com/docker/machine/libmachine/log)
BuildRequires: golang(github.com/docker/machine/libmachine/mcnerror)
BuildRequires: golang(github.com/docker/machine/libmachine/mcnflag)
BuildRequires: golang(github.com/docker/machine/libmachine/mcnutils)
BuildRequires: golang(github.com/docker/machine/libmachine/provision)
BuildRequires: golang(github.com/docker/machine/libmachine/provision/pkgaction)
BuildRequires: golang(github.com/docker/machine/libmachine/provision/serviceaction)
BuildRequires: golang(github.com/docker/machine/libmachine/shell)
BuildRequires: golang(github.com/docker/machine/libmachine/ssh)
BuildRequires: golang(github.com/docker/machine/libmachine/state)
BuildRequires: golang(github.com/docker/machine/libmachine/swarm)
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/inconshreveable/go-update)
BuildRequires: golang(github.com/kardianos/osext)
BuildRequires: golang(github.com/olekukonko/tablewriter)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(github.com/pkg/browser)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(k8s.io/kubernetes/pkg/api)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/v1)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/unversioned)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd/api)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd/api/latest)
BuildRequires: golang(k8s.io/kubernetes/pkg/runtime)
%endif

Requires:      golang(github.com/asaskevich/govalidator)
Requires:      golang(github.com/blang/semver)
Requires:      golang(github.com/docker/go-units)
Requires:      golang(github.com/docker/machine/drivers/hyperv)
Requires:      golang(github.com/docker/machine/drivers/virtualbox)
Requires:      golang(github.com/docker/machine/drivers/vmwarefusion)
Requires:      golang(github.com/docker/machine/libmachine)
Requires:      golang(github.com/docker/machine/libmachine/auth)
Requires:      golang(github.com/docker/machine/libmachine/drivers)
Requires:      golang(github.com/docker/machine/libmachine/drivers/plugin)
Requires:      golang(github.com/docker/machine/libmachine/drivers/plugin/localbinary)
Requires:      golang(github.com/docker/machine/libmachine/engine)
Requires:      golang(github.com/docker/machine/libmachine/host)
Requires:      golang(github.com/docker/machine/libmachine/log)
Requires:      golang(github.com/docker/machine/libmachine/mcnerror)
Requires:      golang(github.com/docker/machine/libmachine/mcnflag)
Requires:      golang(github.com/docker/machine/libmachine/mcnutils)
Requires:      golang(github.com/docker/machine/libmachine/provision)
Requires:      golang(github.com/docker/machine/libmachine/provision/pkgaction)
Requires:      golang(github.com/docker/machine/libmachine/provision/serviceaction)
Requires:      golang(github.com/docker/machine/libmachine/shell)
Requires:      golang(github.com/docker/machine/libmachine/ssh)
Requires:      golang(github.com/docker/machine/libmachine/state)
Requires:      golang(github.com/docker/machine/libmachine/swarm)
Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/google/go-github/github)
Requires:      golang(github.com/inconshreveable/go-update)
Requires:      golang(github.com/kardianos/osext)
Requires:      golang(github.com/olekukonko/tablewriter)
Requires:      golang(github.com/pborman/uuid)
Requires:      golang(github.com/pkg/browser)
Requires:      golang(github.com/pkg/errors)
Requires:      golang(github.com/spf13/cobra)
Requires:      golang(github.com/spf13/pflag)
Requires:      golang(github.com/spf13/viper)
Requires:      golang(golang.org/x/crypto/ssh)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(k8s.io/kubernetes/pkg/api)
Requires:      golang(k8s.io/kubernetes/pkg/api/v1)
Requires:      golang(k8s.io/kubernetes/pkg/client/unversioned)
Requires:      golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd)
Requires:      golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd/api)
Requires:      golang(k8s.io/kubernetes/pkg/client/unversioned/clientcmd/api/latest)
Requires:      golang(k8s.io/kubernetes/pkg/runtime)

Provides:      golang(%{import_path}/cmd/minishift/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/minishift/cmd/config) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/minishift/cmd/openshift) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/cluster) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/config) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/constants) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/kubeconfig) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/machine) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/openshiftversions) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/sshutil) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/tests) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minikube/update) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/cache) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/clusterup) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/config) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/docker) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/openshift) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/provisioner) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/registration) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/minishift/util) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/testing) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/testing/cli) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util/archive) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util/github) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util/os) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util/os/atexit) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/version) = %{version}-%{release}
Provides:      golang(%{import_path}/test/integration) = %{version}-%{release}
Provides:      golang(%{import_path}/test/integration/util) = %{version}-%{release}

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
BuildRequires: golang(github.com/DATA-DOG/godog)
BuildRequires: golang(github.com/DATA-DOG/godog/gherkin)
BuildRequires: golang(github.com/docker/machine/drivers/fakedriver)
BuildRequires: golang(github.com/docker/machine/libmachine/provision/provisiontest)
%endif

Requires:      golang(github.com/DATA-DOG/godog)
Requires:      golang(github.com/DATA-DOG/godog/gherkin)
Requires:      golang(github.com/docker/machine/drivers/fakedriver)
Requires:      golang(github.com/docker/machine/libmachine/provision/provisiontest)

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

%gotest %{import_path}/cmd/minishift/cmd
%gotest %{import_path}/cmd/minishift/cmd/config
%gotest %{import_path}/cmd/minishift/cmd/openshift
%gotest %{import_path}/pkg/minikube/cluster
%gotest %{import_path}/pkg/minikube/constants
%gotest %{import_path}/pkg/minikube/kubeconfig
%gotest %{import_path}/pkg/minikube/machine
%gotest %{import_path}/pkg/minikube/openshiftversions
%gotest %{import_path}/pkg/minikube/sshutil
%gotest %{import_path}/pkg/minishift/cache
%gotest %{import_path}/pkg/minishift/config
%gotest %{import_path}/pkg/minishift/provisioner
%gotest %{import_path}/pkg/minishift/registration
%gotest %{import_path}/pkg/minishift/util
%gotest %{import_path}/pkg/util
%gotest %{import_path}/pkg/util/github
%gotest %{import_path}/test/integration
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc ROADMAP.md README.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc ROADMAP.md README.md CONTRIBUTING.md
%endif

%changelog
* Mon Mar 20 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.0.0-0.1.gite05dbec
- First package for Fedora

