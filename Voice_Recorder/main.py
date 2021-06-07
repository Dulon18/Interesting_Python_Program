#pip install sounddevice
#pip install scipy

import sounddevice
from scipy.io.wavfile import write

# Here f means frequency it will be 44100 or 48000
f=48000

second=int(input("Enter the time duration in second : "))
print('Recording......')
record_voice = sounddevice.rec(int(second*f),samplerate=f,channels=2)
sounddevice.wait()

write("Python_Recoder.wav",f,record_voice)
print("Finished\nPlease Check it on your folder")
