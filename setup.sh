echo "Enable volume automount"
mkdir /mnt/volume
chmod 770 /mnt/volume
cp /etc/fstab /etc/fstab.backupd
echo '/dev/sda1 /mnt/volume' >> /etc/fstab
echo "Installing required packages"
pip install -r requirements.txt
echo "Copying service"
cp ./services/*.service /etc/systemd/system/
echo "Staring services"
systemctl enable alarm.service
systemctl enable serial.service
systemctl daemon-reload
systemctl start alarm.service
systemctl start serial.service
