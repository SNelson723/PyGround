# Installed wavio
import wavio as wv

# Installed sounddevice
import sounddevice as sd

# installed scipy
from scipy.io.wavfile import write

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start the recorder with the given values of duration and freq
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record the audio
sd.wait()

# using scipy to save the audio file
write("recording0.wav", freq, recording)

# using wavio to save the recording
wv.write("recording1.wav", recording, freq, sampwidth=2)