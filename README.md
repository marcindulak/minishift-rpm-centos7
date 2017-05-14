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
        $ vagrant ssh -c "sudo su - -c 'if \$(cat /etc/redhat-release | grep -qi \"release 7\") && ! rpm -q epel-release; then yum -y install https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm; fi'"
        $ vagrant ssh -c "sudo su - -c 'yum -y install spectool tito'"
        $ vagrant ssh -c "sudo su - -c 'mkdir -p /root/rpmbuild/{SOURCES,RPMS}'"
        $ vagrant ssh -c "sudo su - -c 'echo [minishift] > /etc/yum.repos.d/minishift.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo baseurl=file:///root/rpmbuild/RPMS >> /etc/yum.repos.d/minishift.repo'"
        $ vagrant ssh -c "sudo su - -c 'echo gpgcheck=0 >> /etc/yum.repos.d/minishift.repo'"

Build RPM of the minishift executable:

        $ vagrant ssh -c "sudo su - -c 'cd /vagrant&& bash build_local.sh'"


-------
License
-------

MIT

