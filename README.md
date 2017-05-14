-----------
Description
-----------

Builds available at https://copr.fedorainfracloud.org/coprs/marcindulak/minishift/


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

Build RPM of the minishift executable:

        $ vagrant ssh -c "sudo su - -c 'cd /vagrant&& bash build_local.sh'"


------------------
Build RPMS on copr
------------------

One option to build RPMS on https://copr.fedorainfracloud.org/ is to use https://github.com/dgoodwin/tito
In order to avoid storing of RPM sources in a git repository https://git-annex.branchable.com/ can be used.
The initial setup of `git-annex` consists of just `git annex init`.
Setting up `tito` for `git-annex` consists of `tito init&& sed -i 's/tito.builder.Builder/tito.builder.GitAnnexBuilder/' .tito/tito.props`.

See an example here https://m0dlx.com/blog/Reproducible_builds_on_Copr_with_tito_and_git_annex.html

The workflow:

- in order to add a new package to `tito` and sources to `git-annex`, e.g. `golang-github-docker-machine`:

    $ gofed github2spec --project docker --repo machine --force  # adjust the required commit, and fill in other missing details manually
    $ bash git_annex_br.sh
    $ git commit && git push
    $ cd golang-github-docker-machine&& tito tag --keep-version --no-auto-changelog
    $ cd -&& git commit && git push&& git push --tags
    $ # cd golang-github-docker-machine&& tito --srpm  # if you want to build locally SRPM

On `copr` web-interface create `New package` and use the following settings:

    Package name: golang-github-google-go-github
    Git URL: https://github.com/marcindulak/minishift-rpm-centos7
    Git directory: golang-github-google-go-github

Note that using `tito` with `git-annex` is currently broken on `copr`: https://bugzilla.redhat.com/show_bug.cgi?id=1426033

- in order to remove a package and sources, e.g. `golang-github-docker-machine`:

    $ git annex drop --force golang-github-docker-machine
    $ rm -rf golang-github-docker-machine&& git add golang-github-docker-machine  # and then git commit && git push


-------
License
-------

MIT

