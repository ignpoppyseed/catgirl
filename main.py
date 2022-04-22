from email import message
from typing_extensions import Required
import discord
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
from discord import guild
from bottoken import TOKEN
from images import possumIMG
#from happy import happyResponse
from responses import complimentResponse, motivateResponse, insultResponse

# sets bot info on start
bot = commands.Bot(case_insensitive=True, command_prefix=">",activity= discord.Activity(type=discord.ActivityType.listening, name="catgirl asmr"), status=discord.Status.online)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help') #disables the built in help command (fuck the built in help command)


# login info
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content.lower() == 'hello catgirl':
        await message.channel.send(f'hello {message.author}!')
    if message.content.lower() == 'do you love me catgirl':
        await message.channel.send(f'No, {message.author} no one does.')

    if isinstance(message.channel, discord.channel.TextChannel):    
        if message.content.lower().startswith('im '):
            await message.channel.send(f'Hi{message.content[2:]}, i\'m catgirl.')

    if isinstance(message.channel, discord.channel.TextChannel):
        if message.content.lower().startswith('i\'m '):
            await message.channel.send(f'Hi{message.content[3:]}, i\'m catgirl.')

    if isinstance(message.channel, discord.channel.TextChannel):
        if "kys" in message.content.lower():
            await message.channel.send(f'Hey {message.author.mention}, that\'s not nice!')

    if isinstance(message.channel, discord.channel.TextChannel):
        if "kms" in message.content.lower():
            await message.channel.send(f'{message.author.mention}, pls dont')

    if isinstance(message.channel, discord.channel.TextChannel):
        if "sad" in message.content.lower():
            await message.channel.send(f'Hey {message.author.mention}, wanna talk about it?')

#wip conversational abilites 
#    if isinstance(message.channel, discord.channel.DMChannel):
#        if "happy" in message.content.lower():
#            randHappy = random.randrange(0, len(happyResponse))
#            await message.author.send(happyResponse[randHappy])

#    if isinstance(message.channel, discord.channel.DMChannel):
#        if "good" in message.content.lower():
#            randHappy = random.randrange(0, len(happyResponse))
#            await message.author.send(happyResponse[randHappy])

    if isinstance(message.channel, discord.channel.DMChannel):
            print(f'{message.author}> {message.content}')

    await bot.process_commands(message)

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
    randPoss = random.randrange(0, len(possumIMG))
    await ctx.send(possumIMG[randPoss])

@slash.slash(
    name="catgirl",
    description="call and response test",
)
async def _slash(ctx:SlashContext):
    await ctx.send('yeah?')

@slash.slash(
    name="query",
    description="shows information about the bot",
)
async def _slash(ctx:SlashContext):
    await ctx.send(
'This server is running catgirl Beta!\n\
catgirl is written by poppy#0001 in Python 3\n\
Always open source @ github.com/ignpoppyseed/catgirl\n\
catgirl\'s pronouns are she/they\n\
`Thank you for helping test catgirl!`\n\
')

@slash.slash(
    name="help",
    description="catgirl help menu",
)
async def _slash(ctx:SlashContext):
    await ctx.send(
'Weclome to catgirl!\n\
**Commands:**\n\
/help - Shows this menu.\n\
/query - Shows information about catgirl.\n\
/catgirl - Call and response test.\n\
/possum - Sends a random possum image.\n\
/nobitches (option) - Sends a user chosen no bitches image.\n\
/compliment - Have catgirl compliment someone.\n\
/insult - Have catgirl insult someone.\n\
/motivate - Have catgirl motivate someone.\
')

@slash.slash(
    name="compliment",
    description="have catgirl compliment someone!",
    options=[
        create_option(
            name="user",
            description="Select a user to compliment!",
            required=True,
            option_type=6,
        )
    ]
)
async def _slash(ctx:SlashContext, user:str):
    randComp = random.randrange(0, len(complimentResponse))
    await ctx.send(user.mention+' '+complimentResponse[randComp])

@slash.slash(
    name="insult",
    description="have catgirl insult someone!",
    options=[
        create_option(
            name="user",
            description="Select a user to insult!",
            required=True,
            option_type=6,
        )
    ]
)
async def _slash(ctx:SlashContext, user:str):
    randInsult = random.randrange(0, len(insultResponse))
    await ctx.send(user.mention+' '+insultResponse[randInsult])

@slash.slash(
    name="motivate",
    description="have catgirl motivate someone!",
    options=[
        create_option(
            name="user",
            description="Select a user to motivate!",
            required=True,
            option_type=6,
        )
    ]
)
async def _slash(ctx:SlashContext, user:str):
    randMoto = random.randrange(0, len(motivateResponse))
    await ctx.send(user.mention+' '+motivateResponse[randMoto])

'''@slash.slash(
    name="dm",
    description="have catgirl insult you!",
    options=[
        create_option(
            name="user",
            description="select a user to DM",
            required=True,
            option_type=6,
        ),
        create_option(
            name="message",
            description="Message to send user",
            required=True,
            option_type=3,
        )
    ]
)
async def _slash(ctx:SlashContext, user:str, message:str):
    per2dm=user
    await ctx.send(user.name+' says: '+message)
    await ctx.per2dm.send(user.name+' says: '+message) '''

bot.run(TOKEN)