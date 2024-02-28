

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
    #find (letters form matrix without spaces form top starting from the left side)\n
    (cords for word multiplayer (if exist if not type n)\n    type only two numbers with coordinates for example "11" - first row, first column\n
    (cords for double letter or n if empty)\n    (cords for tripple letter or empty) '''
     await ctx.send(message)


@bot.command()
async def find(ctx, matrix_string: str, multiplayer: tuple = None, double_letter: tuple = None, triple_letter: tuple = None ):
    special_cords = {"double": double_letter, "triple": triple_letter, "multiplayer": multiplayer,}
    if multiplayer != None:
        special_cords["multiplayer"] = mod.str_to_cords_tuple(multiplayer)
    if double_letter != None:
        special_cords["double"] = mod.str_to_cords_tuple(double_letter)
    if triple_letter != None:
            special_cords["triple"] = mod.str_to_cords_tuple(triple_letter)


    try:
        response = mod.formated_words_form_sting_response(matrix_string, special_cords)
    except:
        response = "Something went wrong try again. Make sure values are correct"
    await ctx.send(f"{response}")


bot.run(TOKEN)


