import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('CaPy is ready!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('E aí, tranquilo? Seja bem-vindo(a) ao melhor servidor do Discord do Brasil (fonte: Eu mesmo). Eu sou o CaPy, o bot desse servidor e eu tô aqui pra te ajudar. Se quiser saber meus comandos é só mandar ".ajuda" que eu te respondo. Vlw flw!')

    # Commands
    @commands.command()
    async def ping(self, context):
        await context.send('pong')

    # TODO: Finish implementation.
    @commands.command()
    async def ajuda(self, context):
        await context.author.send('pong')


def setup(client):
    client.add_cog(General(client))
