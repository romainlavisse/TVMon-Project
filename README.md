# TVMon-Project

## Requirements 
### access right 

to add the access right for tshark 
you have to do this: 
```
sudo dpkg-reconfigure wireshark-commun
sudo adduser $USER wireshark
```
and reboot your computer

to enable start tc netem from python:

$visudo
add a line to file /etc/sudoers  

username ALL=(ALL) NOPASSWD: /sbin/tc

### python librairys
```
pip install [libName]
```
you have to install:
* pathlib
* pandas
* matplotlib
* psutil
* tkinter

### linux application
``` 
sudo apt-get install [applicationName]
```
you have to install:
* vlc
* tshark
* wmctrl

## how to use 

```
python3 demoTVm.py

```
