from calendar import c
from typing_extensions import Required
import discord
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
from discord import guild
from bottoken import TOKEN
from images import possumIMG
from images import bitchesIMG

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix=">",activity= discord.Activity(type=discord.ActivityType.listening, name="catgirl asmr"), status=discord.Status.online)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help') #disables the built in help command


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
    if message.content.startswith('im '):
        await message.channel.send(f'Hi{message.content[2:]}, i\'m catgirl.')
    if message.content.startswith('i\'m '):
        await message.channel.send(f'Hi{message.content[3:]}, i\'m catgirl.')
    if message.content.startswith('Im '):
        await message.channel.send(f'Hi{message.content[2:]}, i\'m catgirl.')
    if message.content.startswith('I\'m '):
        await message.channel.send(f'Hi{message.content[3:]}, i\'m catgirl.')
    

    await bot.process_commands(message)

#These are the prefix based commands and do not require discord_slash to work.
#@bot.command() <- Do not change
#async def query(ctx): <- replace "query" with name of command
    #await ctx.send('PLACEHOLDER') <- replace "PLACEHOLDER" with text you would like to send

#@bot.command()
#async def query(ctx): # The name of the function is the name of the command
#    await ctx.send('this server is running catgirl2, by poppy.') # ctx.send sends text in chat

#@bot.command()
#async def catgirl(ctx): # the yellow text before (ctx) is the name of the command
#    await ctx.send('yeah?') # the text in apostrophes is what is sent clientside

#@bot.command()
#async def help(ctx): # The name of the function is the name of the command
#    await ctx.send('catgirl2 Help Menu!\nPrefix: >\n>query - information about the bot\n>multi (arg) (arg) - multiply two arguments\n>wiki (arg) - search wikihow\npossum - generate random possum image') # ctx.send sends text in chat

#@bot.command()
#async def multi(ctx, arg1, arg2): # The name of the function is the name of the command
#    await ctx.send('That equals '+str(int(arg1) ** int(arg2))) # ctx.send sends text in chat

#@bot.command()
#async def wiki(ctx, wiki): # The name of the function is the name of the command
#    await ctx.send('https://www.wikihow.com/wikiHowTo?search='+(str(wiki))) # ctx.send sends text in chat

@bot.command()
async def possum(ctx):
    numImg = random.randrange(0, 21)
    await ctx.send(('this command is deprecated, please use slash commands')+possumIMG[numImg])

#These are slash commands and require discord_slash

#@slash.slash(
#    name="catgirl",
#    description="slash test",
#    guild_ids=[951027740256137226, 878297527412224041],
#    options=[
#        create_option(
#            name="option",
#            description="option1",
#            required=True,
#            option_type=3,
#            choices=[
#                create_choice(
#                    name="choice1",
#                    value="you selected: choice1"
#                ),
#                create_choice(
#                    name="choice2",
#                    value="you selected choice2"
#                )
#            ]
#        )
#    ]
#)
#async def _slash(ctx:SlashContext, option:str):
#    await ctx.send(option)
@slash.slash(
    name="nobitches",
    description="tell someone how few bitches they have",
    options=[
        create_option(
            name="option",
            description="choose which meme to send",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="miranda",
                    value="https://i.imgur.com/5pPodXt.jpg"
                ),
                create_choice(
                    name="shrek",
                    value="https://i.imgur.com/WpYZGNF.jpg"
                ),
                create_choice(
                    name="geico",
                    value="https://i.imgur.com/NUB1gZe.jpg"
                ),
                create_choice(
                    name="T",
                    value="https://i.imgur.com/DFnA5lY.jpg"
                ),
                create_choice(
                    name="titanfall",
                    value="https://i.imgur.com/QF1qbLx.jpg"
                ),
                create_choice(
                    name="dog",
                    value="https://i.imgur.com/q3jIczW.jpg"
                ),
                create_choice(
                    name="squidward",
                    value="https://i.imgur.com/J5vhQ6L.jpg"
                ),
                create_choice(
                    name="patrick",
                    value="https://i.imgur.com/qi2eRGc.jpg"
                ),
                create_choice(
                    name="all",
                    value="https://i.imgur.com/HBg5o2A.jpg"
                ),
                create_choice(
                    name="none",
                    value="https://i.imgur.com/5iQoPDR.jpg"
                ),
                create_choice(
                    name="zade",
                    value="https://i.imgur.com/8WGl3jM.jpg"
                ),
            ]
        )
    ]
)
async def _slash(ctx:SlashContext, option:str):
    await ctx.send(option)

@slash.slash(
    name="possum",
    description="send random possum",
)
async def _slash(ctx:SlashContext):
    randPoss = random.randrange(0, 21)
    await ctx.send(possumIMG[randPoss])

@slash.slash(
    name="catgirl",
    description="call and response test",
)
async def _slash(ctx:SlashContext):
    await ctx.send('yeah?')

@slash.slash(
    name="query",
    description="information about the bot",
)
async def _slash(ctx:SlashContext):
    await ctx.send('This server is running catgirl Beta!\ncatgirl is written by poppy#0001 in Python 3\ncatgirl\'s pronouns are she/they\n`Thank you for helping test catgirl!`\n')

@slash.slash(
    name="help",
    description="catgirl help menu",
)
async def _slash(ctx:SlashContext):
    await ctx.send('Weclome to catgirl!\n**Commands:**\n/help - Shows this menu.\n/query - Shows information about catgirl.\n/catgirl - Call and response test.\n/possum - Sends a random possum image.\n/nobitches (option) - Sends a user chosen no bitches image.')

bot.run(TOKEN)