import discord
import asyncio
import random
from discord.ext import commands
from bottoken import TOKEN
from images import possumIMG

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix=">",activity= discord.Activity(type=discord.ActivityType.watching, name="poppy test catgirl"), status=discord.Status.dnd)
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
        await message.channel.send(f'Hi{message.content[2:]}, im dad.')

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

possumImage=["https://cdn.discordapp.com/attachments/946618549428969512/951281697226362891/IMG_9335.jpg", 
"https://cdn.discordapp.com/attachments/946618549428969512/946619221830418493/IMG_9036.jpg", 
"https://cdn.discordapp.com/attachments/946618549428969512/946619222119841862/IMG_9037.jpg"]

@bot.command()
async def possum(ctx):
    numImg = random.randrange(0, 21)
    await ctx.send(possumIMG[numImg])

bot.run(TOKEN)