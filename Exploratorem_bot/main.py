#thirt-party import
import discord
from discord.ext import commands

#build-in import


#local import
from components import webcam, microphone, directory



bot_token = "MTA5MDMyOTIwMzI4MDQ0OTY2Ng.Gr6zoD.DPltyUkRKv906QK2dlMjRK48rehwLZkz-q2GyM"


intents = discord.Intents.default()
intents.members=True


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
       


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")  



@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")


@bot.command()
async def detect_user(ctx):
    detector = webcam.WebcamDetection()
    await detector.webcam_detection(ctx)

@bot.command()
async def record_audio(ctx):
    recorder = microphone.AudioRecord()
    await recorder.record_audio(ctx)
    
@bot.command()
async def scan_directory(ctx, path):
    path == None
    if path is not None:
        scanner = directory.scanDirectory()
        await scanner.scan_directory(ctx, path)
    
    else:
        ctx.send(f"No path has been given!")

if __name__ == "__main__":
    bot.run(bot_token)
