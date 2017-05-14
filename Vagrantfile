# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX = ENV.fetch('BOX', 'bento/fedora-25')

Vagrant.configure(2) do |config|
  config.vm.define "minishift-rpm-centos7" do |machine|
    machine.vm.box = BOX
    machine.vm.box_url = BOX
  end
  config.vm.define "minishift-rpm-centos7" do |machine|
    machine.vm.provision :shell, :inline => "hostname minishift-rpm-centos7", run: "always"
    machine.vm.provision :shell, :inline => "yum -y install wget git rpm-build spectool createrepo"
    machine.vm.provision :shell, :inline => "if `cat /etc/redhat-release | grep -qi 'release 7'` && ! rpm -q epel-release; then yum -y install https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm; fi"
    machine.vm.provision :shell, :inline => "yum -y install spectool gofed tito git-annex"
    machine.vm.provision :shell, :inline => "mkdir -p /root/rpmbuild/{SOURCES,RPMS}"
    machine.vm.provision :shell, :inline => "echo [local] > /etc/yum.repos.d/local.repo"
    machine.vm.provision :shell, :inline => "echo baseurl=file:///root/rpmbuild/RPMS >> /etc/yum.repos.d/local.repo"
    machine.vm.provision :shell, :inline => "echo gpgcheck=0 >> /etc/yum.repos.d/local.repo"
  end
end

