from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from env import DEFAULT_SOUND_PATH

playback_pr = None
alarm = AudioSegment.from_file(DEFAULT_SOUND_PATH + 'alarm.wav')
abort_alarm = AudioSegment.from_file(DEFAULT_SOUND_PATH + 'no_alarm.wav')


def __play(file):
    print('play')
    global playback_pr
    if playback_pr is not None and playback_pr.is_alive():
        playback_pr.terminate()
    playback_pr = Process(target=play, args=(file,))
    playback_pr.start()


def play_alarm():
    print('alarm')
    __play(alarm)


def play_abort_alarm():
    print('abort')
    __play(abort_alarm)

