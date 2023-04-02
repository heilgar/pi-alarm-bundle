import time
from os.path import exists
from pydub import AudioSegment, playback
from multiprocessing import Process
from env import ALARM_F_NAME, DEFAULT_SOUND_PATH, NO_F_NAME, VOLUME_SOUND_PATH, SILENCE_F_NAME

alarm_playback = None
silence_playback = None
is_silence = False

# TODO: Compose logic to class
# TODO: Refactor logic


def __get_file_path(alarm: bool = False) -> str:
    if alarm:
        file_name = ALARM_F_NAME
    else:
        file_name = NO_F_NAME

    if exists(VOLUME_SOUND_PATH + file_name):
        return VOLUME_SOUND_PATH + file_name
    else:
        return DEFAULT_SOUND_PATH + file_name


def get_silence_file():
    if exists(VOLUME_SOUND_PATH + SILENCE_F_NAME):
        return VOLUME_SOUND_PATH + SILENCE_F_NAME

    return DEFAULT_SOUND_PATH + SILENCE_F_NAME


def __play(file_path: str | None = None):
    if not file_path:
        return

    global alarm_playback
    file_to_play = AudioSegment.from_file(file_path)

    if alarm_playback is not None and alarm_playback.is_alive():
        alarm_playback.kill()

    alarm_playback = Process(target=playback.play, args=(file_to_play,))
    alarm_playback.start()
    toggle_silence(file_to_play)


# silence should be refactored
def __play_silence(wait_for_file):
    global silence_playback
    global is_silence

    if is_silence:
        if not silence_playback or not silence_playback.is_alive():
            silence_playback = Process(target=__play_silence_pr, args=(wait_for_file,))
            silence_playback.start()
    else:
        silence_playback.kill()


def __play_silence_pr(wait_for_file):
    if wait_for_file:
        time.sleep(wait_for_file.duration_seconds - 1)
    '''
        While alarm we have to send signal to block another signals in audio network
    '''
    while True:
        file = AudioSegment.from_file(get_silence_file())
        sp = playback._play_with_simpleaudio(file)
        time.sleep(file.duration_seconds - 1)


def toggle_silence(wait_for_file):
    global is_silence
    is_silence = not is_silence
    __play_silence(wait_for_file)


def play_alarm():
    __play(__get_file_path(True))


def play_abort_alarm():
    __play(__get_file_path(False))
