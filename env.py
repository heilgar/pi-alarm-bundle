import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_SOUND_PATH = os.getenv('DEFAULT_SOUND_PATH', './resources')
API_PATH = os.getenv('API_PATH', 'https://api.invalid/v1/status/device')


def serial() -> str:
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
