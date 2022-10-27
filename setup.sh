echo "Setup env"
apt update
wget -qO - https://raw.githubusercontent.com/tvdsluijs/sh-python-installer/main/python.sh | sudo bash -s 3.10.0
apt install -y ffmpeg
echo "Installing required packages"
pip install -r requirements.txt
echo "Enable volume automount"
mkdir /mnt/volume
chmod 770 /mnt/volume
cp /etc/fstab /etc/fstab.backupd
echo '/dev/sda1 /mnt/volume fat32 auto,nofail,x-systemd.device-timeout=30  0 0' >> /etc/fstab
echo "Copying service"
cp ./services/*.service /etc/systemd/system/
echo "Staring services"
systemctl enable alarm.service
systemctl enable serial.service
systemctl daemon-reload
systemctl start alarm.service
systemctl start serial.service
