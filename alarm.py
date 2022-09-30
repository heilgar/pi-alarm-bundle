# #!/usr/bin/python

from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

from serial import get_serial

STATE = False
bState = False
buttonPressed = 0

# GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
B_PIN = 13

GPIO.setwarnings(False)
GPIO.setup(B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

DEFAULT_SOUND_PATH = '/root/bootstrap/pi-alarm-bundle/'

def button_callback(channel):
    global STATE
    global buttonPressed
    global bState

    STATE = True
    bState = True

    now = datetime.now()

    if buttonPressed == 0:
        buttonPressed = now
        play_alarm()

    if buttonPressed != 0:
        diff = now - buttonPressed
        diff = diff.total_seconds() / 60
        if diff > 1.0:
            buttonPressed = 0
            play_disable_alarm()


def get_server_state():
    import requests
    import json
    global buttonPressed

    r = requests.get(
        'https://api.invalid/v1/status/device',
        headers={'Authorization': get_serial()}
    )
    content = r.content.decode('utf-8')
    data = json.loads(content)
    r.close()
    status = data['alarm']
    global STATE
    if status == 'Yes':
        STATE = True
    else:
        STATE = False

    return STATE


def play_alarm():
    song = AudioSegment.from_mp3(DEFAULT_SOUND_PATH + 'alarm.mp3')
    play(song)


def play_disable_alarm():
    song = AudioSegment.from_mp3(DEFAULT_SOUND_PATH + 'no_alarm.mp3')
    play(song)

GPIO.add_event_detect(B_PIN, GPIO.RISING, callback=button_callback)

print('start')
while True:
    prevState = STATE
    for i in range(6):
        sleep(1)
        get_server_state()

        if STATE:
            if prevState == STATE:
                continue
            prevState = STATE
            play_alarm()
        else:
            if prevState == STATE:
                continue
            prevState = STATE
            play_disable_alarm()
