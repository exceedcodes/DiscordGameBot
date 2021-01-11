import discord
from discord.ext import commands
import datetime
from datetime import datetime
from config import *
from game import *

bot = commands.Bot(command_prefix=PREFIX, description="Test Bot for the discord.py")
MESSAGEID = 797355209558327357


@bot.event
async def on_ready():
    print(f"I am alive!")


@bot.command(pass_context=True)
async def hello(ctx, name: str):
    await ctx.send(f"Welcome {name}")


@bot.event
async def on_raw_reaction_add(payload):
    if MESSAGEID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == 'reactnative':
            role = discord.utils.get(guild.roles, name="React Native")
        elif emoji == 'python':
            role = discord.utils.get(guild.roles, name="Python")
        elif emoji == 'cpp':
            role = discord.utils.get(guild.roles, name="C++")
        elif emoji == 'code':
            role = discord.utils.get(guild.roles, name="Coder")
        elif emoji == 'college':
            role = discord.utils.get(guild.roles, name="College")
        elif emoji == "🎮":
            role = discord.utils.get(guild.roles, name="Gamer")
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    if MESSAGEID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        print(emoji)
        if emoji == 'reactnative':
            role = discord.utils.get(guild.roles, name="React Native")
        elif emoji == 'python':
            role = discord.utils.get(guild.roles, name="Python")
        elif emoji == 'cpp':
            role = discord.utils.get(guild.roles, name="C++")
        elif emoji == 'code':
            role = discord.utils.get(guild.roles, name="Coder")
        elif emoji == 'college':
            role = discord.utils.get(guild.roles, name="College")
        elif emoji == "🎮":
            role = discord.utils.get(guild.roles, name="Gamer")
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member not found")


@bot.command(pass_context=True)
async def bye(ctx):
    embed = discord.Embed(
        title="Welcome To Exceed",
        url='https://www.youtube.com/channel/UCp1qAHqhn5Scv1tPtiHnf7w',
        color=0x1abc9c
    )
    embed.add_field(name="Please Select a Role from the reactions below",
                    value=
                        "React Native - <:reactnative:797345705311862814> "
                        "\nPython - <:python:797345704934113280>"
                        "\nC++ - <:cpp:797345704879456306>"
                        "\nCoder(AllSeer) - <:code:797354382555480105>"
                        "\n College - <:college:797345705227976764>",)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('<:python:797345704934113280>')
    await msg.add_reaction('<:reactnative:797345705311862814>')
    await msg.add_reaction('<:cpp:797345704879456306>')
    await msg.add_reaction('<:cpp:797345704879456306>')
    await msg.add_reaction('<:code:797354382555480105>')
    await msg.add_reaction('<:college:797345705227976764>')
    await msg.add_reaction("🎮")


@bot.command(pass_context=True)
async def clear(ctx, amount: str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))


@bot.command(pass_context=True)
@commands.has_role("Gamer")
async def game(ctx):
    await LoadGames(ctx, bot)


bot.run(TOKEN, bot=True, reconnect=True)
