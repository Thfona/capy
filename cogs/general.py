import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('E aí, tranquilo?\n\nSeja bem-vindo(a) ao melhor servidor do Discord do Brasil.\n\nEu sou o CaPy, o bot desse servidor e eu tô aqui pra te ajudar.\nSe quiser saber meus comandos é só mandar ".ajuda" que eu te respondo.\n\nVlw flw!')

    # Commands
    @commands.command()
    async def ping(self, context):
        await context.send(f'Pong! ({round(self.client.latency * 1000)}ms)')

    @commands.command(aliases=['codigo', 'repositorio'])
    async def github(self, context):
        await context.author.send('https://github.com/Thfona/capy')

    @commands.command()
    async def ajuda(self, context):
        help_text = ('**Comandos:**'
                    '\n\n:satellite_orbital:  Ping: Mostra a latência das minhas respostas (e também serve pra jogar ping-pong). :ping_pong:```bash\n.ping```'
                    '\n:smiley_cat:  GitHub: Te levo até o meu código fonte pra você ver tudinho. :flushed:```bash\n.github```'
                    '\n:four_leaf_clover:  Sorte: Me faz uma pergunta sobre o futuro e eu vou te dizer se vai rolar ou não. :thinking:```bash\n.sorte [pergunta]```')

        await context.author.send(help_text)


def setup(client):
    client.add_cog(General(client))
