import librosa
import numpy
import matplotlib.pyplot as plt
import matplotlib.style as ms
import librosa.display
import IPython.display
import sklearn
import os
import os.path

rootdir = "D:\datasets\environmental-sound-classification-50\\audio\\44100"

for parent, dirnames, filenames in os.walk(rootdir):

    for filename in filenames:
        print(filename)




