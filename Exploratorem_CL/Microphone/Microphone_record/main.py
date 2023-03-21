import sounddevice as sd

# Set up recording parameters
fs = 44100  # Sample rate
duration = 5  # Duration in seconds

# Record audio from microphone
print('Recording...')
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

# Wait for recording to finish
sd.wait()

# Play back recorded audio
print('Playing back...')
sd.play(recording, fs)
