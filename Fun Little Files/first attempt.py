import pyaudio
import numpy as np
import tkinter as tk
import time
import os

low = .03
med = .08

root = tk.Tk()
root.overrideredirect(True) #removes movement bar and red X

frameCnt = 3
frames = [tk.PhotoImage(file='talking.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    if(ind<=low):
        frame = frames[0]
    elif(ind<=med):
        frame = frames[1]
    else:
        frame = frames[2]
    label.configure(image=frame)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", 'white')
    root.config(bg='white')
    ind = getsound()
    root.after(10, update, ind)

maxValue = 2**16
bars = 35
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, input_device_index=3, frames_per_buffer=1024)
label = tk.Label(root)
label.config(bg='white')
label.pack()
def getsound():
    data = np.frombuffer(stream.read(1024),dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    peak = (peakL + peakR) / 2
    print(peak)
    return peak
root.after(0, update, 0)
root.mainloop()
    

