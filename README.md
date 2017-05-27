# Raspberry Pi 3
# system version: 2017-04-10-raspbian-jessie

# WiringPi installation:
    1.
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install git-core
    git clone https://github.com/WiringPi/WiringPi.git
    cd wiringPi
    git pull
    ./build
    2.
    https://git.drogon.net/?p=wiringPi;a=summary
    tar xfz wiringPi-96344ff.tar.gz  //The name of the wiringPi package is probably not 96344ff, please change according to the actual situation.
    cd wiringPi-96344ff
    ./build

# I2C installation:
    sudo apt-get install i2c-tools
    sudo apt-get install python-smbus

    sudo nano /etc/modules
#### Add the following two lines:
	i2c-bcm2708
	i2c-dev
#### Exit nano Ctrl+X and enter Y

	sudo nano /boot/config.txt
#### Add at the end:
	dtoverlay=pi3-disable-bt
	enable_uart=1
#### Find '#dtparam=i2c_arm=on' and delete '#'
#### Exit nano Ctrl+X and enter Y

# Serial configuration:
    sudo clone https://github.com/pyserial/pyserial.git
    cd pyserial

    sudo python setup.py install
    sudo nano /boot/cmdline.txt
#### Delete all, and then add:
    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
#### Exit nano Ctrl+X and enter Y

    sudo reboot