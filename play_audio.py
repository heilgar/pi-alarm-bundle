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


def __play(file_path: str | None = None):
    if not file_path:
        return

    global alarm_playback
    file = AudioSegment.from_file(file_path)

    if alarm_playback is not None and alarm_playback.is_alive():
        alarm_playback.kill()

    alarm_playback = Process(target=playback.play, args=(file,))
    alarm_playback.start()


# silence should be refactored
def __play_silence():
    global silence_playback
    global is_silence

    if is_silence:
        if not silence_playback or not silence_playback.is_alive():
            silence_playback = Process(target=__play_silence_pr)
            silence_playback.start()
    else:
        silence_playback.kill()


def __play_silence_pr():
    '''
        While alarm we have to send signal to block another signals in audio network
    '''
    while True:
        file = AudioSegment.from_file(DEFAULT_SOUND_PATH + SILENCE_F_NAME)
        sp = playback._play_with_simpleaudio(file)
        sp.wait_done()



def play_silence():
    global is_silence
    is_silence = True
    __play_silence()


def stop_silence():
    global is_silence
    is_silence = False
    __play_silence()


def play_alarm():
    play_silence()
    __play(__get_file_path(True))


def play_abort_alarm():
    stop_silence()
    __play(__get_file_path(False))
