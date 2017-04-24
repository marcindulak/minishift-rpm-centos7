# Bundled dependencies sources
%global bundled_source_start 10
%global bundled_source_end 18


# github.com/docker/machine
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/docker/machine/drivers/hyperv) = 0.9.0
%else
Provides:           bundled(github.com/docker/machine) = 0.9.0
Source10:           https://github.com/docker/machine/archive/v0.9.0.tar.gz
%endif


BuildRequires:      golang(github.com/google/go-github/github)


BuildRequires:      golang(github.com/inconshreveable/go-update)


# github.com/mitchellh/mapstructure
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/mitchellh/mapstructure) = db1efb556f84b25a0a13a04aad883943538ad2e0
%else
Provides:           bundled(github.com/mitchellh/mapstructure) = db1efb556f84b25a0a13a04aad883943538ad2e0
Source11:           https://github.com/mitchellh/mapstructure/archive/db1efb556f84b25a0a13a04aad883943538ad2e0/mapstructure-db1efb5.tar.gz
%endif


BuildRequires:      golang(github.com/kardianos/osext)


BuildRequires:      golang(github.com/olekukonko/tablewriter)


BuildRequires:      golang(github.com/pkg/browser)


# github.com/spf13/viper
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/spf13/viper) = 382f87b929b84ce13e9c8a375a4b217f224e6c65
%else
Provides:           bundled(github.com/spf13/viper) = 382f87b929b84ce13e9c8a375a4b217f224e6c65
Source12:           https://github.com/spf13/viper/archive/382f87b929b84ce13e9c8a375a4b217f224e6c65/viper-382f87b.tar.gz
%endif


BuildRequires:      golang(github.com/xeipuuv/gojsonschema)


# github.com/blang/semver
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/blang/semver) = 3.5.0
%else
Provides:           bundled(github.com/blang/semver) = 3.5.0
Source13:           https://github.com/blang/semver/archive/v3.5.0.tar.gz
%endif


BuildRequires:      golang(github.com/docker/go-units)


# github.com/pkg/errors
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/pkg/errors) >= 0.8.0, golang(github.com/pkg/errors) < 1.8.0
%else
Provides:           bundled(github.com/pkg/errors) = 0.8.0
Source14:           https://github.com/pkg/errors/archive/v0.8.0.tar.gz
%endif


# github.com/jteeuwen/go-bindata
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/jteeuwen/go-bindata) >= 3.0.7, golang(github.com/jteeuwen/go-bindata) < 3.1.0
%else
Provides:           bundled(github.com/jteeuwen/go-bindata) = 3.0.7
Source15:           https://github.com/jteeuwen/go-bindata/archive/v3.0.7.tar.gz
%endif


BuildRequires:      golang(github.com/spf13/cobra/doc)


BuildRequires:      golang(github.com/spf13/pflag)


BuildRequires:      golang(golang.org/x/crypto/ssh)


BuildRequires:      golang(golang.org/x/oauth2)


BuildRequires:      golang(github.com/cheggaaa/pb)


# github.com/asaskevich/govalidator
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/asaskevich/govalidator) = 5
%else
Provides:           bundled(github.com/asaskevich/govalidator) = 5
Source16:           https://github.com/asaskevich/govalidator/archive/v5.tar.gz
%endif


# github.com/DATA-DOG/godog
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/DATA-DOG/godog) = v0.6.2
%else
Provides:           bundled(github.com/DATA-DOG/godog) = v0.6.2
Source17:           https://github.com/DATA-DOG/godog/archive/v0.6.2.tar.gz
%endif


# github.com/golang/glog
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/golang/glog) = 335da9dda11408a34b64344f82e9c03779b71673
%else
Provides:           bundled(github.com/golang/glog) = 335da9dda11408a34b64344f82e9c03779b71673
Source18:           https://github.com/golang/glog/archive/335da9dda11408a34b64344f82e9c03779b71673/glog-335da9d.tar.gz
%endif


