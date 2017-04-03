yum -y install "compiler(go-compiler)"
spectool -g -R golang-github-asaskevich-govalidator/golang-github-asaskevich-govalidator.spec
rpmbuild -bb golang-github-asaskevich-govalidator/golang-github-asaskevich-govalidator.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/Masterminds/semver)"
yum -y install "golang(github.com/dgrijalva/jwt-go)"
yum -y install "golang(github.com/stretchr/testify/require)"
spectool -g -R golang-github-Azure-go-autorest/golang-github-Azure-go-autorest.spec
rpmbuild -bb golang-github-Azure-go-autorest/golang-github-Azure-go-autorest.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/go-sql-driver/mysql)"
spectool -g -R golang-github-DATA-DOG-go-txdb/golang-github-DATA-DOG-go-txdb.spec
rpmbuild -bb golang-github-DATA-DOG-go-txdb/golang-github-DATA-DOG-go-txdb.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/DATA-DOG/go-txdb)"
spectool -g -R golang-github-DATA-DOG-godog/golang-github-DATA-DOG-godog.spec
rpmbuild -bb golang-github-DATA-DOG-godog/golang-github-DATA-DOG-godog.spec

spectool -g -R golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec
rpmbuild -bb golang-github-inconshreveable-go-update/golang-github-inconshreveable-go-update.spec

spectool -g -R golang-github-pkg-browser/golang-github-pkg-browser.spec
rpmbuild -bb golang-github-pkg-browser/golang-github-pkg-browser.spec

spectool -g -R golang-github-pyr-egoscale/golang-github-pyr-egoscale.spec
rpmbuild -bb golang-github-pyr-egoscale/golang-github-pyr-egoscale.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/davecgh/go-spew/spew)"
spectool -g -R golang-github-vmware-govmomi/golang-github-vmware-govmomi.spec
rpmbuild -bb golang-github-vmware-govmomi/golang-github-vmware-govmomi.spec

yum -y install "golang(github.com/docker/go-units)"
yum -y install "golang(github.com/stretchr/testify/mock)"
yum -y install "golang(github.com/docker/docker/pkg/ioutils)"
yum -y install "golang(golang.org/x/net/context)"
yum -y install "golang(github.com/Sirupsen/logrus)"
yum -y install "golang(github.com/gorilla/mux)"
spectool -g -R golang-github-samalba-dockerclient/golang-github-samalba-dockerclient.spec
rpmbuild -bb golang-github-samalba-dockerclient/golang-github-samalba-dockerclient.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/Azure/azure-sdk-for-go/storage)"
yum -y install "golang(github.com/Azure/go-autorest/autorest)"
yum -y install "golang(github.com/aws/aws-sdk-go/aws)"
yum -y install "golang(github.com/bugsnag/bugsnag-go)"
yum -y install "golang(github.com/codegangsta/cli)"
yum -y install "golang(github.com/digitalocean/godo)"
yum -y install "golang(github.com/docker/docker/pkg/term)"
yum -y install "golang(github.com/pyr/egoscale/src/egoscale)"
yum -y install "golang(github.com/rackspace/gophercloud)"
yum -y install "golang(github.com/samalba/dockerclient)"
yum -y install "golang(github.com/skarademir/naturalsort)"
yum -y install "golang(github.com/vmware/govcloudair)"
yum -y install "golang(github.com/vmware/govmomi)"
yum -y install "golang(golang.org/x/crypto/ssh)"
yum -y install "golang(golang.org/x/oauth2)"
spectool -g -R golang-github-docker-machine/golang-github-docker-machine.spec
rpmbuild -bb golang-github-docker-machine/golang-github-docker-machine.spec

createrepo ~/rpmbuild/RPMS&& yum clean all --enablerepo=minishift --disablerepo='*'
yum -y install "golang(github.com/DATA-DOG/godog)"
yum -y install "golang(github.com/asaskevich/govalidator)"
yum -y install "golang(github.com/blang/semver)"
yum -y install "golang(github.com/docker/machine/libmachine)"
#yum -y install "golang(github.com/google/go-github/github)"  # https://bugzilla.redhat.com/show_bug.cgi?id=1430132
yum -y install "https://kojipkgs.fedoraproject.org//packages/golang-github-google-go-github/0/0.1.git553fda4.fc25/noarch/golang-github-google-go-github-devel-0-0.1.git553fda4.fc25.noarch.rpm"  # https://bugzilla.redhat.com/show_bug.cgi?id=1430132
yum -y install "golang(github.com/inconshreveable/go-update)"
yum -y install "golang(github.com/kardianos/osext)"
yum -y install "golang(github.com/olekukonko/tablewriter)"
yum -y install "golang(github.com/pborman/uuid)"
yum -y install "golang(github.com/pkg/browser)"
yum -y install "golang(github.com/pkg/errors)"
yum -y install "golang(github.com/spf13/cobra)"
yum -y install "golang(k8s.io/kubernetes/pkg/api)"
spectool -g -R golang-github-minishift-minishift/golang-github-minishift-minishift.spec
rpmbuild -bb golang-github-minishift-minishift/golang-github-minishift-minishift.spec

