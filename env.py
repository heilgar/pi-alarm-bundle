import os
from dotenv import load_dotenv

load_dotenv()

B_PIN = int(os.getenv('B_PIN', 13))
DEFAULT_SOUND_PATH = os.getenv('DEFAULT_SOUND_PATH', './resources/')
VOLUME_SOUND_PATH = os.getenv('VOLUME_SOUND_PATH', '/mnt/volume/')
ALARM_F_NAME = os.getenv('ALARM_F_NAME', '1.mp3')
NO_F_NAME = os.getenv('NO_F_NAME', '2.mp3')
SILENCE_F_NAME = os.getenv('SILENCE_F_NAME', '3.mp3')
API_PATH = os.getenv('API_PATH', 'https://api.invalid/v1/status/device')
IS_LOCAL = os.getenv('IS_LOCAL', False)


def serial() -> str:
    if IS_LOCAL:
        return '3A64DB3D-A12F-43ED-88C7-377D542B776A'

    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


if __name__ == '__main__':
    print('Serial: ' + serial())
