import os
from datetime import datetime
import aiohttp

import discord
from discord.ext import commands


token: str = "YOUR TOKEN"
prefix: str = "wd!" # TOTALLY USELESS LOL


bot = commands.Bot(command_prefix=prefix, case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_message(message: discord.Message):
    guild_id = 1158731144519491614
    if message.guild.id == guild_id and message.content == "wec!copy":
        guild = bot.get_guild(guild_id)
        print(guild)
        if guild:
            emotes = guild.emojis
            for emote in emotes:
                print(emote.name)
                url = emote.url
                print(url)
                emoji_ext = url[-4:]
                folder_path = f'emojis/{guild.id}/'
                print(f"Created a emoji folder: {folder_path}")
                os.makedirs(folder_path, exist_ok=True)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        with open(f'{folder_path}{emote.name}{emoji_ext}', 'wb') as f:
                            f.write(await response.read())
            await print('Emotes downloaded successfully.')


@bot.event
async def on_connect():
    print("Logged on as {0.user}".format(bot))

if __name__ == '__main__':
    bot.run(token)