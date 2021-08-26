import os
import discord
from discord.ext import commands
from classes.custom_help_command import CustomHelpCommand

client = commands.Bot(command_prefix='.', help_command=CustomHelpCommand())


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('DARK SOULS: Prepare To Die Edition'))
    print('CaPy is ready!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
