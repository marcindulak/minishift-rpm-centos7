# Bundled dependencies sources
%global bundled_source_start 10
%global bundled_source_end 17


# github.com/docker/machine
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/docker/machine/drivers/hyperv) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/drivers/virtualbox) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/drivers/vmwarefusion) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/auth) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/drivers) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/drivers/plugin) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/drivers/plugin/localbinary) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/engine) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/host) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/log) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/mcnerror) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/mcnflag) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/mcnutils) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/provision) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/provision/pkgaction) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/provision/serviceaction) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/shell) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/ssh) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/state) = 0.11.0
BuildRequires:      golang(github.com/docker/machine/libmachine/swarm) = 0.11.0
%else
# Provides:           bundled(golang(github.com/docker/machine)) = 0.11.0
Source10:           machine-0.11.0.tar.gz
# wget -q https://github.com/docker/machine/archive/v0.11.0.tar.gz -O machine-0.11.0.tar.gz
%endif
%global import_path_10 github.com/docker/machine


# github.com/google/go-github
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/google/go-github/github) = 30a21ee1a3839fb4a408efe331f226b73faac379
%else
# Provides:           bundled(golang(github.com/google/go-github)) = 30a21ee1a3839fb4a408efe331f226b73faac379
Source11:           https://github.com/google/go-github/archive/30a21ee1a3839fb4a408efe331f226b73faac379/go-github-30a21ee.tar.gz
# wget -q https://github.com/google/go-github/archive/30a21ee1a3839fb4a408efe331f226b73faac379/go-github-30a21ee.tar.gz
%endif
%global import_path_11 github.com/google/go-github


BuildRequires:      golang(github.com/inconshreveable/go-update)


BuildRequires:      golang(github.com/mitchellh/mapstructure)


BuildRequires:      golang(github.com/kardianos/osext)


BuildRequires:      golang(github.com/olekukonko/tablewriter)


BuildRequires:      golang(github.com/pkg/browser)


BuildRequires:      golang(github.com/spf13/viper)


BuildRequires:      golang(github.com/xeipuuv/gojsonschema)


# github.com/blang/semver
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/blang/semver) = 3.5.0
%else
# Provides:           bundled(golang(github.com/blang/semver)) = 3.5.0
Source12:           semver-3.5.0.tar.gz
# wget -q https://github.com/blang/semver/archive/v3.5.0.tar.gz -O semver-3.5.0.tar.gz
%endif
%global import_path_12 github.com/blang/semver


BuildRequires:      golang(github.com/docker/go-units)


# github.com/pkg/errors
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/pkg/errors) >= 0.8.0, golang(github.com/pkg/errors) < 1.8.0
%else
# Provides:           bundled(golang(github.com/pkg/errors)) = 0.8.0
Source13:           errors-0.8.0.tar.gz
# wget -q https://github.com/pkg/errors/archive/v0.8.0.tar.gz -O errors-0.8.0.tar.gz
%endif
%global import_path_13 github.com/pkg/errors


BuildRequires:      golang(github.com/spf13/cobra/doc)


BuildRequires:      golang(github.com/spf13/pflag)


BuildRequires:      golang(golang.org/x/crypto/ssh)


BuildRequires:      golang(golang.org/x/oauth2)


# github.com/cheggaaa/pb
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/cheggaaa/pb) = v1.0.13
%else
# Provides:           bundled(golang(github.com/cheggaaa/pb)) = v1.0.13
Source14:           pb-v1.0.13.tar.gz
# wget -q https://github.com/cheggaaa/pb/archive/v1.0.13.tar.gz -O pb-v1.0.13.tar.gz
%endif
%global import_path_14 github.com/cheggaaa/pb


BuildRequires:      golang(github.com/asaskevich/govalidator)


# github.com/DATA-DOG/godog
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/DATA-DOG/godog) = v0.6.2
%else
# Provides:           bundled(golang(github.com/DATA-DOG/godog)) = v0.6.2
Source15:           godog-v0.6.2.tar.gz
# wget -q https://github.com/DATA-DOG/godog/archive/v0.6.2.tar.gz -O godog-v0.6.2.tar.gz
%endif
%global import_path_15 github.com/DATA-DOG/godog


# github.com/golang/glog
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/golang/glog) = 335da9dda11408a34b64344f82e9c03779b71673
%else
# Provides:           bundled(golang(github.com/golang/glog)) = 335da9dda11408a34b64344f82e9c03779b71673
Source16:           https://github.com/golang/glog/archive/335da9dda11408a34b64344f82e9c03779b71673/glog-335da9d.tar.gz
# wget -q https://github.com/golang/glog/archive/335da9dda11408a34b64344f82e9c03779b71673/glog-335da9d.tar.gz
%endif
%global import_path_16 github.com/golang/glog


# github.com/briandowns/spinner
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/briandowns/spinner) = v1.0
%else
# Provides:           bundled(golang(github.com/briandowns/spinner)) = v1.0
Source17:           spinner-v1.0.tar.gz
# wget -q https://github.com/briandowns/spinner/archive/1.0.tar.gz -O spinner-v1.0.tar.gz
%endif
%global import_path_17 github.com/briandowns/spinner


