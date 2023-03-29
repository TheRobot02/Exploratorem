import discord
from discord.ext import commands

def handle_response(messege) -> str:
    p_messege = messege.lower()

    if p_messege == "hello":
        return "Hello!"
    
    if p_messege == "!help"
        return "This is a help messege."
