yum -y update curl curl-devel
# generate current minishift dependencies
pushd minishift
rm -f glide.yaml
wget -q https://raw.githubusercontent.com/minishift/minishift/master/glide.yaml
# https://github.com/marcindulak/minishift-rpm-centos7/issues/5
sed -i 's|gopkg.in/cheggaaa/pb.v1|github.com/cheggaaa/pb|' glide.yaml
# https://github.com/minishift/minishift/issues/814
sed -i 's|version: ~3.0|version: ~3.0.7|' glide.yaml
yum -y install "python-yaml"
python glide2specinc.py > ~/rpmbuild/SOURCES/glide2specinc.inc
cp -fv 830.patch ~/rpmbuild/SOURCES
popd

yum -y install "compiler(go-compiler)"
yum -y install "golang(github.com/docker/go-units)"

# Specific versions needed
# https://github.com/minishift/minishift/issues/828
spectool -g -R golang-github-google-go-github/golang-github-google-go-github.spec
rpmbuild -bb golang-github-google-go-github/golang-github-google-go-github.spec

spectool -g -R golang-github-olekukonko-tablewriter/golang-github-olekukonko-tablewriter.spec
rpmbuild -bb golang-github-olekukonko-tablewriter/golang-github-olekukonko-tablewriter.spec

# https://github.com/minishift/minishift/issues/827
yum -y install "golang(github.com/stretchr/testify/require)"
spectool -g -R golang-github-spf13-jWalterWeatherman/golang-github-spf13-jWalterWeatherman.spec
rpmbuild -bb golang-github-spf13-jWalterWeatherman/golang-github-spf13-jWalterWeatherman.spec

spectool -g -R golang-github-magiconair-properties/golang-github-magiconair-properties.spec
rpmbuild -bb golang-github-magiconair-properties/golang-github-magiconair-properties.spec

# https://github.com/minishift/minishift/issues/828
spectool -g -R golang-github-spf13-cast/golang-github-spf13-cast.spec
rpmbuild -bb golang-github-spf13-cast/golang-github-spf13-cast.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/spf13/cast)"
yum -y install "golang(github.com/magiconair/properties)"
yum -y install "golang(github.com/fsnotify/fsnotify)"
yum -y install "golang(github.com/hashicorp/hcl)"
yum -y install "golang(github.com/mitchellh/mapstructure)"
yum -y install "golang(github.com/pelletier/go-toml)"
yum -y install "golang(github.com/spf13/afero)"
yum -y install "golang(github.com/spf13/jWalterWeatherman)"
yum -y install "golang(github.com/spf13/pflag)"
yum -y install "golang(gopkg.in/yaml.v2)"

spectool -g -R golang-github-spf13-viper/golang-github-spf13-viper.spec
rpmbuild -bb golang-github-spf13-viper/golang-github-spf13-viper.spec

yum -y install bsdiff
spectool -g -R golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec
rpmbuild -bb golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec

spectool -g -R golang-github-pkg-browser/golang-github-pkg-browser.spec
rpmbuild -bb golang-github-pkg-browser/golang-github-pkg-browser.spec

yum -y install "golang(golang.org/x/sys/unix)"
spectool -g -R golang-github-mattn-go-isatty/golang-github-mattn-go-isatty.spec
rpmbuild -bb golang-github-mattn-go-isatty/golang-github-mattn-go-isatty.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/mattn/go-isatty)"
spectool -g -R golang-github-mattn-go-colorable/golang-github-mattn-go-colorable.spec
rpmbuild -bb golang-github-mattn-go-colorable/golang-github-mattn-go-colorable.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/mattn/go-colorable)"
spectool -g -R golang-github-fatih-color/golang-github-fatih-color.spec
rpmbuild -bb golang-github-fatih-color/golang-github-fatih-color.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/fatih/color)"
spectool -g -R golang-github-cheggaaa-pb/golang-github-cheggaaa-pb.spec
rpmbuild -bb golang-github-cheggaaa-pb/golang-github-cheggaaa-pb.spec

spectool -g -R golang-github-asaskevich-govalidator/golang-github-asaskevich-govalidator.spec
rpmbuild -bb golang-github-asaskevich-govalidator/golang-github-asaskevich-govalidator.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/inconshreveable/go-update)"
yum -y install "golang(github.com/kardianos/osext)"
yum -y install "golang(github.com/olekukonko/tablewriter)"
yum -y install "golang(github.com/pkg/browser)"
yum -y install "golang(github.com/spf13/cobra)"
yum -y install "golang(github.com/xeipuuv/gojsonschema)"
yum -y install "golang(golang.org/x/oauth2)"
yum -y install "golang(golang.org/x/crypto/ssh)"
yum -y install "golang(github.com/cheggaaa/pb)"

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
rpmbuild -bb golang-github-samalba-dockerclient/golang-github-samalba-dockerclient.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/samalba/dockerclient)"
yum -y install "golang(github.com/spf13/viper)"
yum -y install "golang(github.com/google/go-github/github)"

# make test dependencies
yum -y install "golang(github.com/go-sql-driver/mysql)"
yum -y install "golang(github.com/Azure/azure-sdk-for-go/storage)"

yum -y install "golang(github.com/Masterminds/semver)"
yum -y install "golang(github.com/dgrijalva/jwt-go)"
yum -y install "golang(github.com/stretchr/testify/require)"
spectool -g -R golang-github-Azure-go-autorest/golang-github-Azure-go-autorest.spec
rpmbuild -bb golang-github-Azure-go-autorest/golang-github-Azure-go-autorest.spec

spectool -g -R golang-github-pyr-egoscale/golang-github-pyr-egoscale.spec
rpmbuild -bb golang-github-pyr-egoscale/golang-github-pyr-egoscale.spec

yum -y install "golang(github.com/davecgh/go-spew/spew)"
spectool -g -R golang-github-vmware-govmomi/golang-github-vmware-govmomi.spec
rpmbuild -bb golang-github-vmware-govmomi/golang-github-vmware-govmomi.spec

spectool -g -R golang-github-armon-consul-api/golang-github-armon-consul-api.spec
rpmbuild -bb golang-github-armon-consul-api/golang-github-armon-consul-api.spec

spectool -g -R golang-github-satori-uuid/golang-github-satori-uuid.spec
rpmbuild -bb golang-github-satori-uuid/golang-github-satori-uuid.spec

spectool -g -R golang-github-shopspring-decimal/golang-github-shopspring-decimal.spec
rpmbuild -bb golang-github-shopspring-decimal/golang-github-shopspring-decimal.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/armon/consul-api)"
yum -y install "golang(github.com/coreos/go-etcd/etcd)"
spectool -g -R golang-github-xordataexchange-crypt/golang-github-xordataexchange-crypt.spec
rpmbuild -bb golang-github-xordataexchange-crypt/golang-github-xordataexchange-crypt.spec

spectool -g -R golang-github-Azure-azure-sdk-for-go/golang-github-Azure-azure-sdk-for-go.spec
rpmbuild -bb golang-github-Azure-azure-sdk-for-go/golang-github-Azure-azure-sdk-for-go.spec

spectool -g -R golang-github-DATA-DOG-go-txdb/golang-github-DATA-DOG-go-txdb.spec
rpmbuild -bb golang-github-DATA-DOG-go-txdb/golang-github-DATA-DOG-go-txdb.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/Azure/azure-sdk-for-go/arm/storage)"
yum -y install "golang(github.com/Azure/go-autorest/autorest)"
yum -y install "golang(github.com/aws/aws-sdk-go/aws)"
yum -y install "golang(github.com/codegangsta/cli)"
yum -y install "golang(github.com/digitalocean/godo)"
yum -y install "golang(github.com/pyr/egoscale/src/egoscale)"
yum -y install "golang(github.com/rackspace/gophercloud)"
yum -y install "golang(github.com/skarademir/naturalsort)"
yum -y install "golang(github.com/vmware/govcloudair)"
yum -y install "golang(github.com/vmware/govmomi)"
yum -y install "golang(github.com/xordataexchange/crypt/config)"
yum -y install "golang(github.com/DATA-DOG/go-txdb)"

# download the dependencies
pushd minishift
IFS_SAVE=$IFS
IFS=$'\n'
for wget in `grep wget  ~/rpmbuild/SOURCES/glide2specinc.inc`; do cmd=`echo $wget | tr -d '#'`&& eval $cmd; done
IFS=$IFS_SAVE
wget -q https://github.com/minishift/minishift/archive/106cf72c58402060cabb224537048aff3e8fcaaf/minishift-106cf72.tar.gz
mv -fv *.tar.gz ~/rpmbuild/SOURCES

rpmbuild -bb minishift.spec

