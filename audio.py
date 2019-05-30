# encoding:utf-8
from aip import AipSpeech
import subprocess,time,tempfile
import pyaudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
audioDev = 0
class BaiduTTS():
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '16143259'
        self.API_KEY = 'Xy3G5WD6E8kEFwSy3FuCgSlm'
        self.SECRET_KEY = '94QyVX3gFvNjTq3fwKGSNmPgApdBFR6u'
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def send_request(self, words):
        result = self.client.synthesis(words, 'zh', 1, {'vol': 5, 'per': 4})
        if not isinstance(result, dict):
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
                f.write(result)
                tmpfile = f.name
                return tmpfile,result,f

    def say(self, words):
        tmpfile, result,f = self.send_request(words)
        # time.sleep(0.5)
        print("file name is"+ tmpfile)
        subprocess.call("play -q %s" % tmpfile, shell=True)

def InitDevice():
    audioDev = pyaudio.PyAudio()
    stream = audioDev.open(format=pyaudio.paInt8,
                    channels=1,
                    rate=16000,
                    output=True)
    return stream

def play(stream, Result):
    stream.write(Result)

