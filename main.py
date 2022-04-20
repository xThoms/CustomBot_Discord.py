#           Notas
#Es obligatorio llenar todas las variables
import discord
from discord.ext import commands
import datetime
import time

TOKEN = str('')
PREFIJO = str('')
BOT_ICON = str('https://example.com/a.png') #Imagen web
BOT_NAME = str('')
ID_BOT = int(1)
BOT_INVITE = str('https://example.com') #Invitacion del bot a un servidor
LOGS_CHANNEL_ID = int(1)
CANAL_ANUNCIOS_GENERALES = int(1)
ACTIVITY_DISCORD_GAME = str('Un juego u oracion')
ON_MESSAGGE_ = False #True o False (Para activar las respuestas a mensajes predeterminados)
ROLE_ADMINISTRADOR = str('') #Nombre del rol administrador

bot = commands.Bot(command_prefix=PREFIJO, help_command=None)

@bot.command(name='s')
async def sumar(ctx, num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)
    c = "sumar"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    chu = num1+" "+num2
    embed.add_field(name="Argumentos del bot", value=chu)
    embed.add_field(name="Respuesta del bot", value=response)
    await channel.send(embed=embed)


@bot.command(name='m') 
async def multiplicar(ctx, num1,num2):
    response = int(num1)*int(num2)
    await ctx.send(response)
    c = "multiplicar"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    chu = num1+" "+num2
    embed.add_field(name="Argumentos del bot", value=chu)
    embed.add_field(name="Respuesta del bot", value=response)
    await channel.send(embed=embed)

@bot.command(name='r')
async def resta(ctx, num1,num2):
    response = int(num1)-int(num2)
    await ctx.send(response)
    c = "resta"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    chu = num1+" "+num2
    embed.add_field(name="Argumentos del bot", value=chu)
    embed.add_field(name="Respuesta del bot", value=response)
    await channel.send(embed=embed)

@bot.command(name='d')
async def divicion(ctx, num1,num2):
    response = int(num1)/int(num2)
    await ctx.send(response)
    c = "divicion"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    chu = num1+" "+num2
    embed.add_field(name="Argumentos del bot", value=chu)
    embed.add_field(name="Respuesta del bot", value=response)
    await channel.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=ACTIVITY_DISCORD_GAME))
    print(f"Bot iniciado correctamente en {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    c = "ping / pong"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value="pong")
    await channel.send(embed=embed)

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()
    c = "say"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value=arg)
    embed.add_field(name="Respuesta del bot", value=arg)
    await channel.send(embed=embed)
   

@bot.command()
async def test(ctx):
    await ctx.send('El modulo general esta funcionando correctamente.')
    c = "test"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value= "El modulo general esta funcionando correctamente.")
    await channel.send(embed=embed)

@bot.command(aliases=["latencia"])
async def realping(ctx):    
    embed = discord.Embed(title="Ping", colour=discord.Color.dark_red(), timestamp=ctx.message.created_at)
    embed.add_field(name="Ping del bot:", value=f"`{round(bot.latency * 1000)} ms`")
    await ctx.send(embed=embed)
    c = "realping"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value= "Embed")
    await channel.send(embed=embed)

@bot.command(aliases=["modulos"])
async  def  module(ctx, v):
    if "musica" == v.lower():
        des = f"""
  **EN DESARROLLO**

  > Prefix:  {PREFIJO}\n
  Hecho por xThoms en Python.\n


    """
        embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_red())
        embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
        embed.set_author(name="Desarrollador xThoms",       
        icon_url=BOT_ICON)
        await ctx.send(embed=embed)
    elif "general" == v.lower():
        des = f"""
  **Comandos generales de {BOT_NAME}:**\n

  - S y M: Se usan para hacer una Suma o Multiplicacion.

  - R y D: Se usan para hacer una Resta o Divición.

  - Info: Muestra informacion del servidor.

  - Help: Muestra un mensaje sobre el bot y sus usos.

  - Ping: Pong.

  - RealPing: Muestra la latencia del bot.

  - MD: Te manda un mensaje :)

  - Say: Sirve para que el bot diga la frase que quieras.

  - Test: Sirve para comprobar que este modulo del bot este funcionando correctamente.

  - Module: Sirve mirar el menu de ayuda de algun modulo.

  > Prefix:  {PREFIJO}\n
  Hecho por xThoms en Python.\n


    """
        embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_red())
        embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
        embed.set_author(name="Desarrollador xThoms",       
        icon_url=BOT_ICON)
        await ctx.send(embed=embed)

    elif "admin" == v.lower():
        des = f"""
  **Comandos administrativos de {BOT_NAME}:**\n

  - Anuncio_u: Envia una mensaje MD a un usuario de parte de los administradores.

  - Anuncio_g: Envia un mensaje general de parte de los administradores.

  - Clear: Elimina mensajes de un canal de texto.

  > Prefix:  {PREFIJO}\n
  Hecho por xThoms en Python.\n


    """
        embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_red())
        embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
        embed.set_author(name="Desarrollador xThoms",       
        icon_url=BOT_ICON)
        await ctx.send(embed=embed)

    elif "administrativo" == v.lower():
        des = f"""
  **Comandos administrativos de {BOT_NAME}:**\n

  - Anuncio_u: Envia una mensaje MD a un usuario de parte de los administradores.

  - Anuncio_g: Envia un mensaje general de parte de los administradores.

  - Clear: Elimina mensajes de un canal de texto.

  > Prefix:  {PREFIJO}\n
  Hecho por xThoms en Python.\n


    """
        embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_red())
        embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
        embed.set_author(name="Desarrollador xThoms",       
        icon_url=BOT_ICON)
        await ctx.send(embed=embed)
    
    else:
        des = f"""
  **Modulos de {BOT_NAME}:**

  - Musica: Modulo musical de {BOT_NAME}.

  - General: Modulo general de {BOT_NAME}.

  - Administrativo: Modulo Administrativo de {BOT_NAME}.

  > Prefix:  !\n
  Hecho por xThoms en Python.\n


    """
        embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_red())
        embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
        embed.set_author(name="Desarrollador xThoms",       
        icon_url=BOT_ICON)
        await ctx.send(embed=embed)
    c = "module"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    a = v
    embed.add_field(name="Argumentos del bot", value=a)
    embed.add_field(name="Respuesta del bot", value= "Embed")
    await channel.send(embed=embed)

@bot.command(aliases=["about"])
async  def  help(ctx):
    des = f"""
  Sobre {BOT_NAME}:\n

  Hola, soy {BOT_NAME} un bot creado por xThoms.

  - Para obtener ayuda sobre los comandos del bot usa "!module" de la siguiente manera: "!module [modulo]", en caso de no conocer los modulos usa "!module modulos"

  > Prefix:  {PREFIJO}
  > Version del Bot: 0.0.1\n
  Hecho por xThoms en Python.\n


    """
    embed = discord.Embed(title=f"Soy {BOT_NAME}",url=BOT_INVITE,description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.dark_red())
    embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
    embed.set_author(name="Desarrollador xThoms",       
    icon_url=BOT_ICON)
    await ctx.send(embed=embed)
    c = "help"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value= "Embed")
    await channel.send(embed=embed)
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_red())
    embed.add_field(name="Servidor creado el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Administrador del servidor", value=f"None format")
    embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=BOT_ICON)
    await ctx.send(embed=embed)
    c = "info"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value= "Embed")
    await channel.send(embed=embed)

@bot.command()
async def md(ctx):
    user = ctx.message.author
    await ctx.message.delete()
    await user.send("😎")
    c = "md"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value="None")
    embed.add_field(name="Respuesta del bot", value= "😎")
    await channel.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_ADMINISTRADOR)
async def anuncio_u(ctx, user: discord.User = None, *, m):
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= m)
    embed.set_author(name="Anuncio de parte de los administradores", icon_url="https://i.imgur.com/CFS4Rqe.png")
    embed.set_footer(text="Desarrollador xThoms")
    await ctx.message.delete()
    await user.send(embed=embed)
    c = "anuncio_u"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    a = str(user)+" "+m
    embed.add_field(name="Argumentos del bot", value=a)
    embed.add_field(name="Respuesta del bot", value= f"Embed")
    await channel.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_ADMINISTRADOR)
async def anuncio_g(ctx, p, *, m):
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= m)
    embed.set_author(name="Anuncio General", icon_url="https://i.imgur.com/CFS4Rqe.png")
    embed.set_footer(text="Desarrollador xThoms")
    channel = bot.get_channel(CANAL_ANUNCIOS_GENERALES)
    if p.lower() == "true":
        embed.add_field(name="Ping:", value=f"[@everyone / @here]")            
        await channel.send("[@everyone / @here]")
        time.sleep(0.05)
        await channel.purge(limit=1)
    elif p.lower() == "false":
        return    
    await ctx.message.delete()
    await channel.send(embed=embed)
    c = "anuncio_g"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    a = p+" "+m
    embed.add_field(name="Argumentos del bot", value=a)
    embed.add_field(name="Respuesta del bot", value= "Embed")
    await channel.send(embed=embed)

@bot.command()
@commands.has_role(ROLE_ADMINISTRADOR)
async def clear(ctx, a):
    a2 = int(a)
    await ctx.message.delete()
    await ctx.channel.purge(limit=a2)
    c = "clear"
    channel = bot.get_channel(LOGS_CHANNEL_ID)
    w = f"El el usuario **{ctx.author.name}** a ejecutado el comando **{c}**"
    embed = discord.Embed(title="",colour=discord.Color.dark_red(), timestamp=ctx.message.created_at,description= w)
    embed.set_author(name="Log", icon_url=BOT_ICON)
    embed.set_footer(text="Desarrollador xThoms")
    embed.add_field(name="Argumentos del bot", value=a)
    embed.add_field(name="Respuesta del bot", value= "None")
    await channel.send(embed=embed)

@bot.listen()
async def on_message(message):
    if ON_MESSAGGE_ == True or ON_MESSAGGE_.lower() == "true":
        if message.author.id == int(ID_BOT):
            return
        elif "hola bot" == message.content.lower():
            await message.channel.send("Hola bro")
        elif "hola" in message.content.lower():
            await message.add_reaction("👋")
        elif "como esta" == message.content.lower():
            await message.add_reaction("🥱") 
        elif "como estas" == message.content.lower():
            await message.add_reaction("🥱")
        elif "como estan" == message.content.lower():
            await message.add_reaction("🥱")

bot.run(TOKEN)