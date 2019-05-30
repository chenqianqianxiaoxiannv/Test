from 百度语音合成 import audio
import pygame
import time
pygame.mixer.init(19200)
ui=ui= audio.BaiduTTS()
results_text='我们去吃饭吧'
tmpfile, result, f = ui.send_request(" ".join(results_text))
pygame.mixer.music.load(tmpfile)
pygame.mixer.music.play()
time.sleep(3)