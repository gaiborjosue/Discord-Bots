import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from dhooks import Webhook
import pyowm
import wikipedia
from youtube_search import YoutubeSearch
import pandas

try:
    from googlesearch import search as sr

except ImportError:
    print("No module with that name exists")

id = "887141482174222357"

client = commands.Bot(command_prefix='!')

owm = pyowm.OWM('0f099a9d2d31309d0cd5667ff52f18dc')


@client.event
async def on_ready():
    activity = discord.Game(name="PhET", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Logged in as")
    print(client.user.name)
    print("---------------")



#Kick members

@client.command(pass_context=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


#INVESTIGACIONES

#book command
@client.command(name="libro")
async def libro(ctx, *, arg):
    l_search = arg
    link_libro = "https://www.google.com/search?tbm=bks&q=" + l_search
    
    final_book = link_libro.replace(" ", "")

    embed2 = discord.Embed(
        title = 'Resultados de la búsqueda',
        description = f':arrow_down: El link que encontré para la búsqueda que hiciste es :arrow_down: {final_book}',
        colour = discord.Colour.green()
    )

    embed2.set_footer(text='Puedes buscar cualquier libro con el comando: !libro')
    embed2.set_author(name='Physics List')

    await ctx.send(embed=embed2)


@client.command()
async def buscar(ctx, *, arg):
    wikipedia.set_lang("es")
    res = wikipedia.summary(arg, sentences=3)

    embedb = discord.Embed(
        title = 'Resultados de la búsqueda',
        description = f'{res}',
        colour = discord.Colour.green()
    )

    embedb.set_footer(text='Puedes investigar conceptos en español usando el comando: !buscar')
    embedb.set_author(name='Physics List')

    await ctx.send(embed=embedb)

@client.command()
async def search(ctx, *, arg):
    wikipedia.set_lang("en")
    res_2 = wikipedia.summary(arg, sentences=3)

    embeds = discord.Embed(
        title = 'Resultados de la búsqueda',
        description = f'{res_2}',
        colour = discord.Colour.green()
    )

    embeds.set_footer(text='Puedes investigar conceptos en ingles usando el comando: !search')
    embeds.set_author(name='Physics List')
    await ctx.send(embed=embeds)


@client.command(aliases=['video', 'vid'])
async def videos(ctx, *, arg):
    results = YoutubeSearch(arg, max_results=10).to_dict()
    res2 = results[0]
    f_video = res2.pop("url_suffix")
    final = "https://youtube.com" + f_video

    embedv = discord.Embed(
        title = 'Resultados de la búsqueda',
        description = f':film_frames: *El video encontrado para tu búsqueda fue* :arrow_right:  {final}',
        colour = discord.Colour.blue()
    )

    embedv.set_footer(text='Puedes investigar videos usando el comando: !video')
    embedv.set_author(name='Physics List')

    await ctx.send(embed=embedv)


@client.command(aliases=['puntaje', 'puntos'])
async def checks(ctx, *, arg):

    df = pandas.read_csv("info.csv", delimiter=",")

    nombre = df["Nombre"].tolist()
    apellido = df["Apellido"].tolist()
    checkS = df["Checks"].tolist()
    deudas = df["Deudas"].tolist()
    recuperaciones = df["Recuperaciones"].tolist()

    resu_t = [x for x in range(len(nombre)) if nombre[x] == f"{arg}"]
    embedh = discord.Embed(
        title = f'Los checks de {arg}',
        description = 
        f"""
        :white_check_mark: *Los checks que tienes disponibles para canjear son* :arrow_right: {checkS[resu_t[0]]}
        """,
        colour = discord.Colour.blue()
    )

    embedh.set_footer(text=
    f"""
    Puedes también ver si tienes pendientes recuperaciones con el comando: !rec {arg}
    Puedes también ver si tienes deudas pendientes con el comando: !deudas {arg}
    """)
    embedh.set_author(name='Physics List')

    await ctx.send(embed=embedh)

@client.command(aliases=['rec', 'oportunidades'])
async def recuperaciones(ctx, *, arg):

    df = pandas.read_csv("info.csv", delimiter=",")

    nombre = df["Nombre"].tolist()
    apellido = df["Apellido"].tolist()
    checkS = df["Checks"].tolist()
    deudas = df["Deudas"].tolist()
    recuperaciones = df["Recuperaciones"].tolist()

    resu_t = [x for x in range(len(nombre)) if nombre[x] == f"{arg}"]
    embedh = discord.Embed(
        title = f'Los checks de {arg}',
        description = 
        f"""
        :white_check_mark: *El número de recuperaciones que tienes pendiente son*  :arrow_right: {recuperaciones[resu_t[0]]}
        """,
        colour = discord.Colour.blue()
    )

    embedh.set_footer(text=
    f"""
    Puedes también ver si tienes pendientes recuperaciones con el comando: !rec {arg}
    Puedes también ver si tienes deudas pendientes con el comando: !deudas {arg}
    """)
    embedh.set_author(name='Physics List')

    await ctx.send(embed=embedh)

@client.command(aliases=['debo'])
async def deudas(ctx, *, arg):

    df = pandas.read_csv("info.csv", delimiter=",")

    nombre = df["Nombre"].tolist()
    apellido = df["Apellido"].tolist()
    checkS = df["Checks"].tolist()
    deudas = df["Deudas"].tolist()
    recuperaciones = df["Recuperaciones"].tolist()

    resu_t = [x for x in range(len(nombre)) if nombre[x] == f"{arg}"]
    embedh = discord.Embed(
        title = f'Los checks de {arg}',
        description = 
        f"""
        :white_check_mark: *El saldo de la deuda pendiente en dólares es*  :arrow_right: {deudas[resu_t[0]]}
        """,
        colour = discord.Colour.blue()
    )

    embedh.set_footer(text=
    f"""
    Puedes también ver si tienes pendientes recuperaciones con el comando: !rec {arg}
    Puedes también ver si tienes deudas pendientes con el comando: !deudas {arg}
    """)
    embedh.set_author(name='Physics List')

    await ctx.send(embed=embedh)
    
client.run('ODg3MTQxNDgyMTc0MjIyMzU3.YT_04w.e00B-XAQdgyn829y27a_GoZXt5A')