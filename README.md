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

### access right to TC and NETEM 
do that
$sudo visudo
Then add a line to opened file /etc/sudoers  

username ALL=(ALL) NOPASSWD: /sbin/tc

### python librarys
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
