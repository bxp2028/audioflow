#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:47:43

@author: 
"""

from pynput import keyboard
import time
import pyaudio
import wave
import sched
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = r"/录音文件/input.wav"

p = pyaudio.PyAudio()
frames = []

def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)

class MyListener(keyboard.Listener):
    def __init__(self):
     super(MyListener, self).__init__(self.on_press, self.on_release)
     self.key_pressed = None
     self.wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
     self.wf.setnchannels(CHANNELS)
     self.wf.setsampwidth(p.get_sample_size(FORMAT))
     self.wf.setframerate(RATE)
    def on_press(self, key):
     if key.char == 'r':
      self.key_pressed = True
     return True

    def on_release(self, key):
     if key.char == 'r':
      self.key_pressed = False
     return True


listener = MyListener()
listener.start()
started = False
stream = None

def recorder():
    global started, p, stream, frames

    if listener.key_pressed and not started:
     # Start the recording
     try:
      stream = p.open(format=FORMAT,
          channels=CHANNELS,
          rate=RATE,
          input=True,
          frames_per_buffer=CHUNK,
          stream_callback = callback)
      print("流活跃:", stream.is_active())
      started = True
      print("开始流")
     except:
      raise

    elif not listener.key_pressed and started:
     print("停止录音")
     stream.stop_stream()
     stream.close()
     p.terminate()
     listener.wf.writeframes(b''.join(frames))
     listener.wf.close()
     print("您应该在当前目录中有一个 wav 文件")
     sys.exit()
    # Reschedule the recorder function in 100 ms.
    task.enter(0.1, 1, recorder,())


print("按住“r”键开始录音")
print("松开“r”键结束录音")
task = sched.scheduler(time.time, time.sleep)
task.enter(0.1, 1, recorder,())
task.run()


import pyttsx3
import pyttsx3
from pyttsx3.voice import Voice
#语音播放 
pyttsx3.speak("你现在在哪里")
pyttsx3.speak("I am fine, thank you")


huayu = "你是谁，你在哪里，你将去向何处？"
def yuyin(hua):
    engine = pyttsx3.init()  ##初始化语音引擎
    rate = engine.getProperty('rate')
    print(f'语速：{rate}')
    # 控制语音播放的速度
    engine.setProperty('rate', 200)
    
    
    volume = engine.getProperty('volume')
    print (f'音量：{volume}')
    # 控制语音播放的音量大小
    engine.setProperty('volume',0.5)
    voice = engine.getProperty('voice')

    v = Voice(id=2, name='财神', languages='Japanese', age=18, gender='male')
    engine.setProperty('voice', v)
    engine.say(hua)
    engine.runAndWait()    #朗读一次
    engine.stop()
yuyin(huayu)


