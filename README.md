-----------
Description
-----------

Packaging minishift https://lists.centos.org/pipermail/centos-devel/2017-March/015723.html

Builds available at https://copr.fedorainfracloud.org/coprs/marcindulak/minishift/


------------------
Build RPMS locally
------------------

It can be done using www.vagrantup.com:

        $ git clone https://github.com/marcindulak/minishift-rpm-centos7
        $ cd minishift-rpm-centos7
        $ BOX='bento/fedora-25' vagrant up

        $ vagrant ssh -c "sudo su - -c 'yum -y install wget git rpm-build spectool createrepo'"
        $ vagrant ssh -c "sudo su - -c 'mkdir -p /root/rpmbuild/{SOURCES,RPMS}'"
        $ vagrant ssh -c "sudo su - -c 'echo [minishift] > /etc/yum.repos.d/minishift.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo baseurl=file:///root/rpmbuild/RPMS >> /etc/yum.repos.d/minishift.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo gpgcheck=0 >> /etc/yum.repos.d/minishift.repo'"

Now, either build RPM of de-bundled minishift library, and dependencies:

        $ vagrant ssh -c "sudo su - -c 'cd /vagrant&& bash debundled.sh'"

or build RPM of the minishift executable using bundled dependencies:

        $ vagrant ssh -c "sudo su - -c 'cd /vagrant&& bash bundled.sh'"


-------
License
-------

MIT

