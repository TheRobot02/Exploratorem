import discord
from discord.ext import commands
#from Exploratorem_CL.Microphone.Microphone_record.main import microphoneRecord
#from Webcam.webcam_live.main import webcamLive



bot_token = "MTA5MDMyOTIwMzI4MDQ0OTY2Ng.Gr6zoD.DPltyUkRKv906QK2dlMjRK48rehwLZkz-q2GyM"

intents = discord.Intents.default()
intents.members=True


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
       


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")





@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")

bot.run(bot_token)

