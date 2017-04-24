# generate current minishift dependencies
pushd minishift
rm -f glide.yaml
wget -q https://raw.githubusercontent.com/minishift/minishift/master/glide.yaml
# major.minor.release for github.com/jteeuwen/go-bindata
sed -i 's|version: ~3.0|version: ~3.0.7|' glide.yaml
yum -y install "python-yaml"
python glide2specinc.py > ~/rpmbuild/SOURCES/glide2specinc.inc
# https://github.com/marcindulak/minishift-rpm-centos7/issues/5
sed -i 's|gopkg.in/cheggaaa/pb.v1|github.com/cheggaaa/pb|' ~/rpmbuild/SOURCES/glide2specinc.inc
popd

yum -y install "compiler(go-compiler)"
yum -y install "golang(github.com/docker/go-units)"
#yum -y install "golang(github.com/google/go-github/github)"  # https://bugzilla.redhat.com/show_bug.cgi?id=1430132
yum -y install "https://kojipkgs.fedoraproject.org//packages/golang-github-google-go-github/0/0.1.git553fda4.fc25/noarch/golang-github-google-go-github-devel-0-0.1.git553fda4.fc25.noarch.rpm"  # https://bugzilla.redhat.com/show_bug.cgi?id=1430132

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

# download the dependencies
IFS_SAVE=$IFS
IFS='\n'
for wget in `grep wget glide2specinc.inc`; do cmd=`echo $wget | tr -d '#'`&& eval $cmd; done
IFS=$IFS_SAVE
wget -q https://github.com/minishift/minishift/archive/cebec68fcf03ae5b5a9c0b808178b542c17215a7/minishift-cebec68.tar.gz
mv -v *.tar.gz ~/rpmbuild/SOURCES

pushd minishift
rpmbuild -bb minishift.spec  # broken build stage

