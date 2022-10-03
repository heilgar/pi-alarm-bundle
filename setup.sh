echo "Installing required packages"
apt -y install ffmpeg rpi.gpio
pip install -r requirements.txt
echo "Copying service"
cp ./services/*.service /etc/systemd/system/
echo "Staring services"

for service in "./services"/*
do
  systemctl enable "$service"
done
systemctl daemon-reload
for service in "./services"/*
do
  systemctl start "$service"
done
