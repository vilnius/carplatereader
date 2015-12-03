Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    # moar powah
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    echo "install Ubuntu's ffmpeg fork - libav"
    sudo apt-get install -y libav-tools

    echo "install openalpr (https://github.com/openalpr/openalpr#binaries)"
    wget -O - http://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
    echo "deb http://deb.openalpr.com/master/ openalpr main" | sudo tee /etc/apt/sources.list.d/openalpr.list
    sudo apt-get update
    sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev

    echo "install openalpr python2 bindings"
    sudo apt-get install -y python-openalpr
  SHELL
end
