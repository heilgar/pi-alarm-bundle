# PI Alarm

Simple script for triggering sound when air alarm on Raspberry PI boards (mod 2,3,4).
Alarm triggered from: lan, and button. 
Default Button PIN 13 or GPIO 27

Requirements:
- Python >=3.10.0
- Raspberry PI 2/3/4

Connection: 
- `ssh pi@<device-ip-addr>`
Note: Device should be in ssh allowance list to use without password

Installation: 
- Clone and run `sudo ./setup.sh`
- Change env vars if not in default location `/root/bootstrap`

Get serial: 
- run a command `sudo less /var/log/syslog | grep Serial`
- or run `python env.py`

Image:
- raspi-latest.img - 4GB microsd - ApplePiBacker for backup/restore
