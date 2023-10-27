# This script installs:
#   - device tree overlay for sc16is752-spi1
#   - wiringpi library
#   - python3
#

#!/bin/bash


echo "Beamercontrol installation started."

echo "Adding devicetree overlay..."
sudo echo dtoverlay=sc16is752-spi1,int_pin=24 >> /boot/config.txt

echo "Installing wiringpi..."
sudo apt-get install wiringpi
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v

echo "Installing python libraries..."
sudo apt-get install python3-pip
sudo pip3 install RPi.GPIO
sudo apt-get install python3-serial

pip3 install "uvicorn[standard]"

# Install systemd service file