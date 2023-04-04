import sounddevice as sd


class microphoneRecord:
    def __init__(self):
        # Set up recording parameters
        self.fs = 44100  # Sample rate
        self.duration = 5  # Duration in seconds

    def record(self):

        #Record audio from microphone
        print('Recording...')
        self.recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)

        # Wait for recording to finish
        sd.wait()

        # Play back recorded audio
        print('Playing back...')
        sd.play(self.recording, self.fs)
