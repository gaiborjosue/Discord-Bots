import discord
from discord.ext import commands
from urllib import parse, request
import re

id  = 'ENTER ID'

client = commands.Bot(command_prefix='!')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Bienvenido al servidor de AmbientaList SAS: {member.mention}, disfruta del contenido, apoyo, tutorias y mucho más que tenemos para ofrecerte!""")

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("D3vil") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="No puedes hacer eso")


@client.event
async def on_message(message):
    message.content.lower()

    id = client.get_guild(756340942151352500)

    channels = ["tutorias", "trabajos-grupales", "estudiar-para-el-examen", "test-bot"]

    private_channels = ["moderator-only", "canal-privado"]

    valid_users = []

    bad_words = ["puta", "chucha", "mierda", "mrd", "vrg", "verga", "Fuck", "FUCK", "bitch", "BITCH"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("Una mala palabra fue dicha")
            await message.channel.purge(limit=1)

    if message.content == "!ayuda":
        embed = discord.Embed(title="Ayuda de AmbientalistBOT", description="Comandos que puedes escribir para reacciones de AmbientaList BOT.")
        embed.add_field(name="!hola", value="AmbientalistBOT Saludará al usuario")
        embed.add_field(name="!recursos", value="Este comando utilizará al bot para mandarte recursos de SAS")
        embed.add_field(name="Censura", value="AmbientaList BOT tiene la capacidad de eliminar mensajes que contengan malas palabras.")
        embed.add_field(name="tutoria", value="Si mandas este mensaje en el canal de tutorias, AmbientaList BOT te guiara y te pondra en contacto con un tutor.")
        embed.add_field(name="!lema", value="Este comando te mostrará el lema de nuestra lista!")
        embed.add_field(name="!nombre", value="Este comando te recordará el nombre de nuestra lista.")
        
        await message.channel.send(content=None, embed=embed)

    
    if message.author == client.user:
        return

    greetings = ["hola", "Hola", "hOla", "holi", "Holi", "que mas", "holis", "Holis", "hi", "Hi", "que tal", "Que tal", "Que mas", "holas", "Holas", "Buenas Tardes", "Buenas", "buenas tardes", "Buenas tardes", "Buenos dias", "Buenos Dias", "buenos dias", "Buenas Noches", "Buenas noches", "buenas noches"]

    for word2 in greetings:
        if message.content.count(word2) > 0:
            await message.channel.send(f"""Hola! Soy AmbientaList, el bot del servidor.""")

    if message.content == "!users":
        await message.channel.send(f"""El numero de Miembros es: {id.member_count}""")

    elif message.content == "!recursos":
        embed2 = discord.Embed(title="No te preocupes, aqui tenemos una amplia lista de recursos:", description="https://linktr.ee/sistemasambientales")
        await message.channel.send(content=None, embed=embed2)

    if message.content == "topas":
        await message.channel.send(f"""Chao!""")

    if message.content == "chao":
        await message.channel.send(f"""Chao, cuidate!""")

    if message.content == "!lema":
        await message.channel.send(f"""Nuestro lema es: Ciencias por la naturaleza.""")

    if message.content == "!nombre":
        await message.channel.send(f"""El nombre de nuestra lista es: AmbientaList""")

    if message.content == "!ambientalist":
        await message.channel.send(f"""Siguenos en instagram: @ambienta_list: https://www.instagram.com/ambienta_list/""")

    if str(message.channel) in channels:
        if message.content == "tutoria":
            await message.channel.send(f"""Ok, entendido. Inmediatamente te contactará un tutor. Si no lo hace, escríbenos por whatsapp: https://wa.link/ljq1pv""")
        if message.content == "tutor":
            await message.channel.send(f"""Ok, entendido. Inmediatamente te contactará un tutor. Si no lo hace, escríbenos por whatsapp: https://wa.link/ljq1pv""")
        if message.content == "tutorias":
            await message.channel.send(f"""Ok, entendido. Inmediatamente te contactará un tutor. Si no lo hace, escríbenos por whatsapp: https://wa.link/ljq1pv""")

    if str(message.channel) in private_channels:
        if message.content == "gracias":
            await message.channel.send(f"""De nada!, siempre es un gusto ayudarlos, :)""")
        if message.content == "pregunta":
            await message.channel.send(f"""Gracias por dejar tu pregunta, en unos momentos el Admin te va a ayudar.""")


@client.command()
async def video(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(\S{11})', html_content.read().decode())
    print(search_results)

client.run('ENTER TOKEN')
