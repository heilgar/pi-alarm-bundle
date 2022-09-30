# #!/usr/bin/python

from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

from serial import get_serial

# GPIO.setmode(GPIO.BCM)

STATE = False
bState = False
buttonPressed = 0
B_PIN = 27


def button_callback(channel):
    global STATE
    global bState
    global buttonPressed

    STATE = True
    bState = True

    now = datetime.now()

    if buttonPressed == 0:
        buttonPressed = now
        play_alarm()

    if buttonPressed not 0:
        diff = now - buttonPressed
        if diff > 1:
            buttonPressed = 0
            play_disable_alarm()


def get_state():
    import requests
    import json

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
    song = AudioSegment.from_mp3('alarm.mp3')
    play(song)


def play_disable_alarm():
    song = AudioSegment.from_mp3('no_alarm.mp3')
    play(song)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(B_PIN, GPIO.RISING, callback=button_callback)

while True:
    print('start')
    prevState = STATE
    for i in range(6):
        sleep(1)
        state = get_state()
        print('received from server', state)
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
