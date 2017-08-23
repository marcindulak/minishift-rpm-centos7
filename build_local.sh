yum -y update curl curl-devel
# generate current minishift dependencies
pushd minishift
# fetch and modify glide.yaml
rm -f glide.yaml
wget -q https://raw.githubusercontent.com/minishift/minishift/0f658ea057b72cac35d6fb22cfa6bec28ef61079/glide.yaml
# https://github.com/marcindulak/minishift-rpm-centos7/issues/5
sed -iv 's|gopkg.in/cheggaaa/pb.v1|github.com/cheggaaa/pb|' glide.yaml
# use the RPM of github.com/jteeuwen/go-bindata https://github.com/minishift/minishift/issues/814
#sed -iv 's|version: ~3.0|version: ~3.0.7|' glide.yaml
sed -iv '/go-bindata/d' glide.yaml
sed -iv '/version: v3.0.7$/d' glide.yaml
# use the RPM of github.com/mitchellh/mapstructure
sed -iv '/version: db1efb556f84b25a0a13a04aad883943538ad2e0$/d' glide.yaml
# use the RPM of github.com/spf13/viper
sed -iv '/version: 382f87b929b84ce13e9c8a375a4b217f224e6c65$/d' glide.yaml
# use the RPM of github.com/asaskevich/govalidator
sed -iv '/version: 5$/d' glide.yaml
# create spec include based on glide.yaml
yum -y install python-yaml
python glide2specinc.py > ~/rpmbuild/SOURCES/glide2specinc.inc
# non-standard version of spinner tarball: 1.0 instead of v1.0
sed -iv 's|spinner/archive/v1.0.tar\.gz|spinner/archive/1.0.tar.gz|' ~/rpmbuild/SOURCES/glide2specinc.inc
cp -fv 830.patch ~/rpmbuild/SOURCES
popd

yum -y install "compiler(go-compiler)"
yum -y install "golang(github.com/docker/go-units)"

# Specific versions needed
# https://github.com/minishift/minishift/issues/893
# Fedora's 553fda4 is newer than glide.lock's 30a21ee1a3839fb4a408efe331f226b73faac379
# # github.com/minishift/minishift/pkg/util/github
# pkg/util/github/github.go:101: not enough arguments in call to client.Repositories.GetReleaseByTag
# pkg/util/github/github.go:104: not enough arguments in call to client.Repositories.GetLatestRelease
# pkg/util/github/github.go:123: not enough arguments in call to client.Repositories.DownloadReleaseAsset
# pkg/util/github/github.go:309: not enough arguments in call to client.Repositories.DownloadReleaseAsset
# the archived releases are no longer accessible https://github.com/google/go-github/issues/705
#git clone https://github.com/google/go-github
#pushd go-github
#git checkout 30a21ee1a3839fb4a408efe331f226b73faac379
#popd
#mv go-github go-github-30a21ee1
#tar zcf go-github-30a21ee1.tar.gz go-github-30a21ee1
#mv go-github-30a21ee1.tar.gz ~/rpmbuild/SOURCES
spectool -g -R golang-github-google-go-github/golang-github-google-go-github.spec
rpmbuild -ba golang-github-google-go-github/golang-github-google-go-github.spec

# Fedora's cca8bbc is too old
# https://bugzilla.redhat.com/show_bug.cgi?id=1320304
# github.com/minishift/minishift/cmd/minishift/cmd/openshift
# cmd/minishift/cmd/openshift/service_list.go:48: table.SetBorders undefined (type *tablewriter.Table has no field or method SetBorders)
# cmd/minishift/cmd/openshift/service_list.go:48: undefined: tablewriter.Border
spectool -g -R golang-github-olekukonko-tablewriter/golang-github-olekukonko-tablewriter.spec
rpmbuild -ba golang-github-olekukonko-tablewriter/golang-github-olekukonko-tablewriter.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/google/go-github/github)"
yum -y install "golang(github.com/olekukonko/tablewriter)"
yum -y install "golang(github.com/spf13/cast)"

yum -y install bsdiff
spectool -g -R golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec
rpmbuild -ba golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec

spectool -g -R golang-github-pkg-browser/golang-github-pkg-browser.spec
rpmbuild -ba golang-github-pkg-browser/golang-github-pkg-browser.spec

yum -y install "golang(golang.org/x/sys/unix)"
spectool -g -R golang-github-mattn-go-isatty/golang-github-mattn-go-isatty.spec
rpmbuild -ba golang-github-mattn-go-isatty/golang-github-mattn-go-isatty.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/mattn/go-isatty)"
spectool -g -R golang-github-mattn-go-colorable/golang-github-mattn-go-colorable.spec
rpmbuild -ba golang-github-mattn-go-colorable/golang-github-mattn-go-colorable.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/mattn/go-colorable)"
spectool -g -R golang-github-fatih-color/golang-github-fatih-color.spec
rpmbuild -ba golang-github-fatih-color/golang-github-fatih-color.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/fatih/color)"
# pinned version of golang-github-cheggaaa-pb in minishift 1.4.1
#spectool -g -R golang-github-cheggaaa-pb/golang-github-cheggaaa-pb.spec
#rpmbuild -ba golang-github-cheggaaa-pb/golang-github-cheggaaa-pb.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/inconshreveable/go-update)"
yum -y install "golang(github.com/kardianos/osext)"
yum -y install "golang(github.com/pkg/browser)"
yum -y install "golang(github.com/spf13/cobra)"
yum -y install "golang(github.com/xeipuuv/gojsonschema)"
yum -y install "golang(golang.org/x/oauth2)"
yum -y install "golang(golang.org/x/crypto/ssh)"
#yum -y install "golang(github.com/cheggaaa/pb)"

yum -y install go-bindata
yum -y install "golang(github.com/fsnotify/fsnotify)"
yum -y install "golang(github.com/hashicorp/hcl)"
yum -y install "golang(github.com/pborman/uuid)"
yum -y install "golang(github.com/pelletier/go-toml)"
yum -y install "golang(github.com/spf13/afero)"
yum -y install docker-devel

yum -y install "golang(github.com/docker/go-units)"
yum -y install "golang(github.com/stretchr/testify/mock)"
yum -y install "golang(github.com/docker/docker/pkg/ioutils)"
yum -y install "golang(golang.org/x/net/context)"
yum -y install "golang(github.com/Sirupsen/logrus)"
yum -y install "golang(github.com/gorilla/mux)"
spectool -g -R golang-github-samalba-dockerclient/golang-github-samalba-dockerclient.spec
rpmbuild -ba golang-github-samalba-dockerclient/golang-github-samalba-dockerclient.spec

# pinned version of golang-github-briandowns-spinner in minishift 1.4.1
#spectool -g -R golang-github-briandowns-spinner/golang-github-briandowns-spinner.spec
#rpmbuild -ba golang-github-briandowns-spinner/golang-github-briandowns-spinner.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=local --disablerepo='*'
yum -y install "golang(github.com/mitchellh/mapstructure)"
yum -y install "golang(github.com/samalba/dockerclient)"
yum -y install "golang(github.com/spf13/viper)"
yum -y install "golang(github.com/asaskevich/govalidator)"

# download the dependencies under ~/rpmbuild/SOURCES
pushd minishift
IFS_SAVE=$IFS
IFS=$'\n'
for wget in `grep wget  ~/rpmbuild/SOURCES/glide2specinc.inc`; do
    cmd=`echo $wget | tr -d '#' | sed 's|-O |-O ~/rpmbuild/SOURCES/|'`
    echo "$cmd -P ~/rpmbuild/SOURCES"
    eval "$cmd -P ~/rpmbuild/SOURCES"
done
IFS=$IFS_SAVE
# see https://github.com/minishift/minishift/issues/1300 - minishift build relies on .git
#wget -q https://github.com/minishift/minishift/archive/0f658ea057b72cac35d6fb22cfa6bec28ef61079/minishift-0f658ea.tar.gz -P ~/rpmbuild/SOURCES
git clone https://github.com/minishift/minishift minishift-0f658ea
pushd minishift-0f658ea
git checkout 0f658ea057b72cac35d6fb22cfa6bec28ef61079
popd
tar zcf minishift-0f658ea.tar.gz minishift-0f658ea
mv minishift-0f658ea.tar.gz ~/rpmbuild/SOURCES
rm -rf minishift-0f658ea

rpmbuild -ba minishift.spec

cp -p /root/rpmbuild/SRPMS/*.src.rpm .

