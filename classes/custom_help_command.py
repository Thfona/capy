import discord
from discord.ext import commands


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        return

    async def send_cog_help(self, cog):
        return

    async def send_group_help(self, group):
        return

    async def send_command_help(self, command):
        return
