# -*- mode: ruby -*-
1;3409;0c# vi: set ft=ruby :

BOX = ENV.fetch('BOX', 'bento/fedora-25')

Vagrant.configure(2) do |config|
  config.vm.define "minishift-rpm-centos7" do |machine|
    machine.vm.box = BOX
    machine.vm.box_url = BOX
  end
  config.vm.define "minishift-rpm-centos7" do |machine|
    machine.vm.provision :shell, :inline => "hostname minishift-rpm-centos7", run: "always"
    machine.vm.provision :shell, :inline => "yum -y install wget git rpm-build spectool createrepo"
  end
end

