import os
import googleapiclient.discovery
import youtube_dl
import discord
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get

youtube_base_url = 'https://www.youtube.com/watch?v='
playlist_id = 'PLyNt_LH-5qNA6QHen_9-OXNHkyY_J9zvB'
youtube_discovery = googleapiclient.discovery.build(
    'youtube', 'v3', developerKey=os.getenv('GOOGLE_API_KEY')
)
lofi_url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'


class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    def is_connected(self, context):
        voice_client = get(context.bot.voice_clients, guild=context.guild)
        return voice_client and voice_client.is_connected()

    # Commands
    @commands.command()
    async def entrar(self, context):
        if (context.author.voice):
            channel = context.message.author.voice.channel

            if (self.is_connected(context)):
                await context.voice_client.move_to(channel)
            else:
                await channel.connect()
        else:
            await context.send('Você precisa tá em um canal de voz pra usar esse comando.')

    @commands.command()
    async def sair(self, context):
        if (context.voice_client):
            await context.guild.voice_client.disconnect()
        else:
            await context.send('Eu não tô em nenhum canal de voz.')

    @commands.command()
    async def parar(self, context):
        voice = get(self.client.voice_clients, guild=context.guild)

        if voice and voice.is_playing():
            voice.stop()
        else:
            await context.send('Não tô tocando nenhum áudio.')

    @commands.command()
    async def yt(self, context, url):
        await self.entrar(context)

        YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        voice = get(self.client.voice_clients, guild=context.guild)

        if voice and voice.is_playing():
            await self.parar(context)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        URL = info['formats'][0]['url']

        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

    @commands.command()
    async def audio(self, context, audio_name):
        playlist_request = youtube_discovery.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50
        )

        playlist_response = playlist_request.execute()

        playlist_items = []

        while playlist_request is not None:
            playlist_response = playlist_request.execute()
            playlist_items += playlist_response['items']
            playlist_request = youtube_discovery.playlistItems(
            ).list_next(playlist_request, playlist_response)

        video_url = ''

        for video in playlist_items:
            snippet = video['snippet']

            title = snippet['title']

            if (title == audio_name):
                resource_id = snippet['resourceId']

                video_id = resource_id['videoId']

                video_url = f'{youtube_base_url}{video_id}'

        if (video_url):
            await self.yt(context, video_url)
        else:
            await context.send('Não encontrei esse áudio.')

    @commands.command()
    async def lofi(self, context):
        await self.yt(context, lofi_url)


def setup(client):
    client.add_cog(Audio(client))
