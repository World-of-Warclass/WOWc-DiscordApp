import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import data.query as query
import data.useful_custom_functions as ucf

load_dotenv()

try:
    token = os.getenv("TOKEN")
    prefix = os.getenv("PREFIX")
except:
    ucf.ErrorMessage("No se ha encontrado el archivo .env").print()

intents = discord.Intents.all()

bot = commands.Bot(prefix, intents=intents)

initial_extensions = ["Cogs.help", "Cogs.ping"]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            ucf.ErrorMessage(f"Failed to load extension {extension}").print()


@bot.event
async def on_ready():
    print()
    ucf.InfoMessage(f"We have logged in as {bot.user}").print()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"
        )
    )
    ucf.InfoMessage(f"We have used discord-py v{discord.__version__}").print()


@bot.command()
async def info(ctx: commands.Context):
    await ctx.send(f"¡Hola {ctx.author.mention}, mi nombre es {bot.user.name}!")


@bot.command()
async def member(ctx: commands.Context, member: discord.Member):
    await ctx.send(f"¡Hola {member.default_avatar}, {member.mention}!")


# TEST VALUE (QUEST ID)
id = 1


@bot.command()
async def embed(ctx: commands.Context):

    embed = discord.Embed(
        title=query.getQuestName(id_quest=id),
        description=query.getQuestDescription(id_quest=id),
        color=discord.Color.random(),
    )
    embed.set_author(name="📋 Tablón de Misiones")
    if query.getQuestExperienceReward(id_quest=id) != 0:
        embed.add_field(
            name="Experiencia",
            value=f"{query.getQuestExperienceReward(id_quest=id)} xp",
        )
    if query.getQuestGoldReward(id_quest=id) != 0:
        embed.add_field(
            name="Piezas de oro", value=f"{query.getQuestGoldReward(id_quest=id)} po"
        )
    embed.set_footer(text=f"Publicado por {query.getTeacher(id_quest=id)}")

    await ctx.send(f"## ¡Aventureros, hay algo nuevo en el tablón de misiones!")
    await ctx.send(embed=embed)


try:
    bot.run(token)
except:
    ucf.ErrorMessage("The app token was not found or cannot be used.").print()
