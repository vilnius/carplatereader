# Repository for _Car Plate Reader_

The scripts contained herein are meant to process the videos and images from public cameras (or
cameras in public transport) to find A-lane or other statically identifiable violators.

### Process and components

![cpr-flow](https://raw.githubusercontent.com/vilnius/carplatereader/master/imgs/cpr-flow.png)
<br/>
<small>[Edit this diagram](https://creately.com/diagram/ilcpovkm1/De4TO3XFXQf4tI6g4q4blBNwA%3D)</small>

### [Server API](docs/API.md)

## Install

Tested on Ubuntu 14.04

### Using vagrant

```bash
vagrant up
vagrant ssh

# inside vagrant
cd /vagrant
```

### Manual install

```bash
# install Ubuntu's ffmpeg fork - libav
sudo apt-get install libav-tools

# install openalpr (https://github.com/openalpr/openalpr#binaries)
wget -O - http://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
echo "deb http://deb.openalpr.com/master/ openalpr main" | sudo tee /etc/apt/sources.list.d/openalpr.list
sudo apt-get update
sudo apt-get install openalpr openalpr-daemon openalpr-utils libopenalpr-dev

# install openalpr python2 bindings
sudo apt-get install -y python-openalpr
```

### Test openalpr

```bash
wget http://plates.openalpr.com/ea7the.jpg
alpr -c us ea7the.jpg

wget http://plates.openalpr.com/h786poj.jpg
alpr -c eu h786poj.jpg
```

## Helpers

### Converting video stream to PNG images

```bash
# if you've installed libav-tools, ffmpeg == avconv
ffmpeg -i /path/to/video.avi -vf fps=1 out/%d.png
```
