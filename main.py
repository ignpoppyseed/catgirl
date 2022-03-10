import discord
import asyncio
import random
from discord.ext import commands
from bottoken import TOKEN
from images import possumIMG

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix=">",activity= discord.Activity(type=discord.ActivityType.listening, name="catgirl asmr"), status=discord.Status.online)
bot.remove_command('help')


# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello catgirl':
        await message.channel.send(f'hello {message.author}!')
    if message.content == 'do you love me catgirl':
        await message.channel.send(f'No, {message.author} no one does.')
    if message.content.startswith('im'):
        await message.channel.send(f'Hi{message.content[2:]}, i\'m catgirl.')
    if message.content.startswith('i\'m'):
        await message.channel.send(f'Hi{message.content[3:]}, i\'m catgirl.')
    if message.content.startswith('Im'):
        await message.channel.send(f'Hi{message.content[2:]}, i\'m catgirl.')
    if message.content.startswith('I\'m'):
        await message.channel.send(f'Hi{message.content[3:]}, i\'m catgirl.')
    

    await bot.process_commands(message)

@bot.command()
async def query(ctx): # The name of the function is the name of the command
    await ctx.send('this server is running catgirl2, by poppy.') # ctx.send sends text in chat

@bot.command()
async def catgirl(ctx): # The name of the function is the name of the command
    await ctx.send('yeah?') # ctx.send sends text in chat

@bot.command()
async def help(ctx): # The name of the function is the name of the command
    await ctx.send('catgirl2 Help Menu!\nPrefix: >\n>query - information about the bot\n>multi (arg) (arg) - multiply two arguments\n>wiki (arg) - search wikihow') # ctx.send sends text in chat

@bot.command()
async def multi(ctx, arg1, arg2): # The name of the function is the name of the command
    await ctx.send('That equals '+str(int(arg1) ** int(arg2))) # ctx.send sends text in chat

@bot.command()
async def wiki(ctx, wiki): # The name of the function is the name of the command
    await ctx.send('https://www.wikihow.com/wikiHowTo?search='+(str(wiki))) # ctx.send sends text in chat

@bot.command()
async def possum(ctx):
    numImg = random.randrange(0, 21)
    await ctx.send(possumIMG[numImg])

bot.run(TOKEN)