pip install -r requirements.txt
cp ./alarm.service /etc/systemd/system/alarm.service
systemctl enable alarm.service
systemctl daemon-reload
systemctl start alarm.service
