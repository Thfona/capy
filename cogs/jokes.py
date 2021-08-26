import random
import discord
from discord.ext import commands


class Jokes(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def sorte(self, context, *args):
        question = ' '.join(args)

        if (not question):
            await context.send('Você precisa me perguntar alguma coisa.')
            return

        responses = ['Com certeza.', 'Decididamente sim.', 'Sem dúvida.', 'Definitivamente.', 'Pode contar com isso.', 'Na minha visão, sim.', 'Provavelmente.', 'Parece que sim.', 'Sim.', 'Tudo indica que sim.', 'A resposta não tá muito clara, tenta de novo depois.',
                     'Me pergunta de novo depois.', 'Melhor eu não te falar agora.', 'Não consigo te responder isso agora.', 'Se concentra e pergunta de novo.', 'Não dá pra contar com isso.', 'Minha resposta é não.', 'Minhas fontes dizem que não.', 'Parece que não.', 'Duvido.']

        await context.send(f'{random.choice(responses)}')


def setup(client):
    client.add_cog(Jokes(client))
