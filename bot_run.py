

import discord
from discord.ext import commands
from dotenv import load_dotenv
import modules as mod
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
async def find(ctx, matrix_string: str, multiplier: tuple = None, double_letter: tuple = None, triple_letter: tuple = None ):
    special_cords = {"double": double_letter, "triple": triple_letter, "multiplier": multiplier,}
    if multiplier != None:
        special_cords["multiplier"] = mod.str_to_cords_tuple(multiplier)
    if double_letter != None:
        special_cords["double"] = mod.str_to_cords_tuple(double_letter)
    if triple_letter != None:
            special_cords["triple"] = mod.str_to_cords_tuple(triple_letter)


    try:
        response = mod.formatted_words_from_string_response(matrix_string, special_cords)
    except:
        response = "Something went wrong try again. Make sure values are correct"
    await ctx.send(f"{response}")


bot.run(TOKEN)


