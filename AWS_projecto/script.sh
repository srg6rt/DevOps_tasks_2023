#!/bin/bash
# sleep until instance is ready
until [[ -f /var/lib/cloud/instance/boot-finished ]]; do
  sleep 1
done

# install apache2
sudo yum update -y
sudo yum install apache2 -y

# make sure apache2 is started
sudo systemctl start apache2

sudo echo "Test web page" > /var/www/html/index.html