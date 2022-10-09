from os.path import exists
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from env import ALARM_F_NAME, DEFAULT_SOUND_PATH, NO_F_NAME, VOLUME_SOUND_PATH

playback_pr = None

def __get_file_path(alarm: bool = False) -> str:
    if alarm:
        file_name = ALARM_F_NAME
    else:
        file_name = NO_F_NAME
    
    if exists(VOLUME_SOUND_PATH + file_name):
        return VOLUME_SOUND_PATH + file_name
    else:
        return DEFAULT_SOUND_PATH + file_name

def __play(file_path: str | None = None):
    if not file_path:
        return

    global playback_pr
    file = AudioSegment.from_file(file_path)

    if playback_pr is not None and playback_pr.is_alive():
        playback_pr.terminate()
    playback_pr = Process(target=play, args=(file,))
    playback_pr.start()


def play_alarm():
    __play(__get_file_path(True))


def play_abort_alarm():
    __play(__get_file_path(False))

