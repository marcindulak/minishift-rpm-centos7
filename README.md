-----------
Description
-----------

**Warning**: this was a PoC project, eventually discouraged by the minishift developers.
See https://github.com/minishift/minishift/issues/1300 for the reasons of abandoning the idea of a debundled minishift RPM.

Builds available at https://copr.fedorainfracloud.org/coprs/marcindulak/minishift/

**Note**: only Fedora RPMS available, no CentOS 7 yet!


-------------------------------
Build RPMS locally with Vagrant
-------------------------------

It can be done using www.vagrantup.com:

        $ git clone https://github.com/marcindulak/minishift-rpm-centos7
        $ cd minishift-rpm-centos7
        $ BOX='bento/fedora-25' vagrant up

        $ vagrant ssh -c "sudo su - -c 'yum -y install wget git rpm-build spectool createrepo'"
        $ vagrant ssh -c "sudo su - -c 'if \$(cat /etc/redhat-release | grep -qi \"release 7\") && ! rpm -q epel-release; then yum -y install https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm; fi'"
        $ vagrant ssh -c "sudo su - -c 'yum -y install spectool gofed tito git-annex'"
        $ vagrant ssh -c "sudo su - -c 'mkdir -p /root/rpmbuild/{SOURCES,RPMS}'"
        $ vagrant ssh -c "sudo su - -c 'echo [local] > /etc/yum.repos.d/local.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo baseurl=file:///root/rpmbuild/RPMS >> /etc/yum.repos.d/local.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo gpgcheck=0 >> /etc/yum.repos.d/local.repo'"

Build RPM of the `minishift` executable:

        $ vagrant ssh -c "sudo su - -c 'cd /vagrant&& bash build_local.sh'"

[build_local.sh](build_local.sh) performs the following stages:

- extract the `minishift` build dependencies by parsing [`minishift`'s glide.yaml](https://github.com/minishift/minishift/blob/master/glide.yaml) using [minishift/glide2specinc.py](minishift/glide2specinc.py) and save this information as [minishift/glide2specinc.inc](minishift/glide2specinc.inc) to be included in the [minishift/minishift.spec](minishift/minishift.spec) file. Ideally one should use [glide.lock](https://github.com/minishift/minishift/blob/master/glide.lock) instead of [glide.yaml](https://github.com/minishift/minishift/blob/master/glide.yaml) as the former contains more dependencies and all the dependencies are versioned by their commit ids in [glide.lock](https://github.com/minishift/minishift/blob/master/glide.lock), but the [glide.lock](https://github.com/minishift/minishift/blob/master/glide.lock) file contains as of today 44 dependencies vs 20 in [glide.yaml](https://github.com/minishift/minishift/blob/master/glide.yaml), and those do not include the dependencies of the dependencies themselves. Therefore I initially decided to package as RPMS only the dependencies listed explicitly in [glide.yaml](https://github.com/minishift/minishift/blob/master/glide.yaml) and use the RPMS provided already by `Fedora` for the remaining dependencies. See discussion [`minishift` #828](https://github.com/minishift/minishift/issues/828).

- build and install all the dependencies discovered above, plus the additional dependencies discovered while running `minishift`'s `make test` [`minishift` #895](https://github.com/minishift/minishift/issues/895).

- download the sources of the `minishift's` dependencies, which are explicitly versioned in the [glide.yaml](https://github.com/minishift/minishift/blob/master/glide.yaml) file, and the source of `minishift` itself.

- build the RPM of `minishift`.


------------------
Build RPMS on copr
------------------

One option to build RPMS on https://copr.fedorainfracloud.org/ is to use https://github.com/dgoodwin/tito
In order to avoid storing of RPM sources in a git repository https://git-annex.branchable.com/ can be used.
The initial setup of `git-annex` consists of just `git annex init`.
Setting up `tito` for `git-annex` consists of `tito init` followed by `sed -i 's/tito.builder.Builder/tito.builder.GitAnnexBuilder/' .tito/tito.props`.

See an example here https://m0dlx.com/blog/Reproducible_builds_on_Copr_with_tito_and_git_annex.html and the discussion https://github.com/domcleal/librarian-puppet-copr/issues/2

The workflow:

- in order to add a new package to `tito` and sources to `git-annex`, e.g. `golang-github-docker-machine`:

      $ gofed github2spec --project docker --repo machine --force  # adjust the required commit, and fill in other missing details manually
      $ bash git_annex_br.sh
      $ git commit && git push
      $ cd golang-github-docker-machine&& tito tag --keep-version --no-auto-changelog
      $ cd -&& git push&& git push --tags
      $ # cd golang-github-docker-machine&& tito --srpm  # if you want to build locally SRPM

  Push the `git-annex` branch (https://git-annex.branchable.com/tips/centralized_git_repository_tutorial/on_GitHub/)

      $ git push origin master git-annex 

  On `copr` web-interface create `New package` and use the following settings:

      Package name: golang-github-google-go-github
      Git URL: https://github.com/marcindulak/minishift-rpm-centos7
      Git directory: golang-github-google-go-github

  Note that using `tito` with `git-annex` seems currently broken on `copr`: https://bugzilla.redhat.com/show_bug.cgi?id=1450950

  If changing the RPMS sources belonging to `minishift` itself use `git_annex_minishift.sh` instead of `git_annex_br.sh`.

- in order to remove a package and sources, e.g. `golang-github-docker-machine`:

      $ git annex drop --force golang-github-docker-machine
      $ rm -rf golang-github-docker-machine&& git add golang-github-docker-machine
      $ git commit && git push

Suggested build order on `copr`:

- golang-github-google-go-github
- golang-github-olekukonko-tablewriter
- golang-github-inconshreveable-go-update
- golang-github-pkg-browser
- golang-github-mattn-go-isatty
- golang-github-mattn-go-colorable
- golang-github-fatih-color
- golang-github-samalba-dockerclient
- minishift


-------
License
-------

MIT

