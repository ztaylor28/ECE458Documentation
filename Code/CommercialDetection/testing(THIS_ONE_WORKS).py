import time
import os
import struct
from tkinter import TclError
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import statistics as ss
import math

while True:
    pa = pyaudio.PyAudio()
    bit_fmt = pyaudio.paFloat32
    stream = pa.open(format=bit_fmt,
                         channels=1,
                         rate=44100,
                         frames_per_buffer=4096,
                         input=True,
                         output=True,
                         )
    stream.start_stream()
    try:
        while stream.is_active():
            buffer = stream.read(4096)
            decoded = np.fromstring(buffer, 'Float32')
            decodedsquared = decoded * decoded*10000
            logrules = (np.log2((decodedsquared*100+1))/np.log2(4))*10
            print(np.round(np.mean(logrules)))
        stream.stop_stream()
        stream.close()
        pa.terminate()
    except OSError as e:
        sys.stderr.write(f'Error: {e}')