

import discord
from discord.ext import commands
from dotenv import load_dotenv
import modules as m
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "#", intents=intents)



@bot.command()
async def info(ctx):
     message = '''This is how you specify the find command 
    #find (letters from matrix without spaces from top starting from the left side)\n
    (coords for word multiplier (if exist if not type n)\n    type only two numbers with coordinates for example "11" - first row, first column\n
    (coords for double letter or n if empty)\n    (coords for triple letter or empty) '''
     await ctx.send(message)


@bot.command()
async def find(ctx, matrix_string: str):
    try:
        response = m.bot_formatted_leaderboard(matrix_string)
    except:
        response = "Something went wrong try again. Make sure values are correct"
    await ctx.send(f"{response}")


bot.run(TOKEN)


