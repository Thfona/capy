import os
import random
import discord
from discord.ext import commands, tasks
from classes.custom_help_command import CustomHelpCommand

client = commands.Bot(command_prefix='.', help_command=CustomHelpCommand())

status_list = ['Dark Souls Remastered', 'Fallout: New Vegas', 'The Elder Scrolls V: Skyrim', 'The Witcher 3: Wild Hunt', 'Cyberpunk 2077', 'Resident Evil Village', 'Resident Evil 2', 'Resident Evil 4', 'Grand Theft Auto: San Andreas', 'Grand Theft Auto: Vice City', 'Grand Theft Auto V', 'Red Dead Redemption II', 'Sekiro: Shadows Die Twice', 'Horizon Zero Dawn', 'Silent Hill 2', 'VALORANT', 'League of Legends', 'Among Us', 'Counter-Strike: Global Offensive', 'Forza Horizon 5', 'Halo: The Master Chief Collection', 'Halo Infinite', 'Don\'t Starve', 'Don\'t Starve Together', 'The Elder Scrolls III: Morrowind', 'The Elder Scrolls IV: Oblivion Remastered', 'Brawlhalla', 'Path of Exile', 'Call of Duty: Warzone', 'Call of Duty: Black Ops 6', 'Heroes of the Storm', 'Overwatch 2', 'Hearthstone', 'Left 4 Dead 2', 'Elden Ring',
               'Minecraft', 'Portal 2', 'Marvel Rivals', 'Terraria', 'Mirror\'s Edge', 'Hades', 'Hades II', 'Killing Floor 2', 'Tomb Raider', 'Street Fighter VI', 'Tekken 8', 'Life is Strange', 'Nioh 2', 'Hollow Knight', 'Saints Row IV', 'Final Fantasy XVI', 'Final Fantasy XIII', 'Final Fantasy XII', 'Mortal Kombat 1', 'Injustice 2', 'The Longest Journey', 'Tom Clancy\'s Rainbow Six Siege', 'Smite', 'Doom: Eternal', 'Borderlands 3', 'Spyro Reignited Trilogy', 'Crash Bandicoot N\'Sane Trilogy', 'Crash Bandicoot 4: It\'s About Time', 'Fable Anniversary', 'Bastion', 'To The Moon', 'Bayonetta', 'Undertale', 'Papers, Please', 'Darkest Dungeon', 'Bad Rats', 'DRAGON BALL FighterZ', 'Super Meat Boy', 'Temtem', 'The Elder Scrolls Online', 'Killer Instinct', 'Bully: Scholarship Edition', 'Fallout 2', 'Amnesia: Rebirth', 'Dishonored']


@client.event
async def on_ready():
    set_status.start()
    print('CaPy is ready!')

@tasks.loop(hours=2)
async def set_status():
    await client.change_presence(activity=discord.Game(random.choice(status_list)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
