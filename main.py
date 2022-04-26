import discord

import time

import datetime

import requests


import random

from discord.ext import commands

from discord_together import DiscordTogether

from webserver import keep_alive

import json

import os


client = commands.Bot(command_prefix=".", help_command=None, intents=discord.Intents.all())

client.remove_command('help')

api_key = "e1fdf18860bc7307dc31e8f31667f033"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
img_hug = ["https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif", 
           "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif", 
           "https://c.tenor.com/4n3T2I239q8AAAAC/anime-cute.gif", 
           "https://c.tenor.com/ztEJgrjFe54AAAAC/hug-anime.gif",
           "https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif", 
           "https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif", 
           "https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif", 
           "https://c.tenor.com/SXk-WqF6PpQAAAAC/anime-hug.gif",
           "https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif",
           "https://c.tenor.com/SPs0Rpt7HAcAAAAC/chiya-urara.gif",
           "https://c.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif", 
           "https://c.tenor.com/jQ0FcfbsXqIAAAAC/hug-anime.gif", 
           "https://c.tenor.com/z2QaiBZCLCQAAAAC/hug-anime.gif", 
           "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif",
           "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", 
           "https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif",
           "https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif", 
           "https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif", 
           "https://c.tenor.com/WpbZhwwj6zAAAAAC/happy-hug.gif",
           "https://c.tenor.com/EnfEuWDXthkAAAAC/hug-couple.gif"]

img_kiss = ["https://c.tenor.com/0VqDj3YhG-sAAAAd/kiss-love-is-love.gif", 
            "https://c.tenor.com/V5U7EcZSGdMAAAAC/pillow-love.gif",
            "https://c.tenor.com/FgYExssph6MAAAAM/kiss-love.gif", 
            "https://c.tenor.com/217aKgnf16sAAAAM/kiss.gif", 
            "https://c.tenor.com/vMAZxue8-zIAAAAM/love-excited.gif",
            "https://c.tenor.com/qwuggqcTDScAAAAM/cat-love.gif", 
            "https://c.tenor.com/lcdIgm9ZR_4AAAAM/soft-kisses.gif", 
            "https://c.tenor.com/KmdTrhPfnAIAAAAM/sleep-kiss.gif"]

img_punch = ["https://c.tenor.com/qc7loiQJZZwAAAAM/punch-bearpunch.gif",
             "https://c.tenor.com/gIaioChTOloAAAAM/cat-cute.gif",
             "https://c.tenor.com/qKTBsktfhSgAAAAM/punch-blue-hoodie.gif" ,
             "https://c.tenor.com/QeTLGgXG6h4AAAAM/angry-cute.gif", 
             "https://c.tenor.com/PYOgLkcIxvoAAAAM/stepbrothers-pummel-punch.gif", 
             "https://c.tenor.com/Q7gJPYeqX_MAAAAM/cat-punch.gif",
             "https://c.tenor.com/TwWbeBz2WtgAAAAM/punch-accidental-punch.gif",
             "https://c.tenor.com/MnFSvXrm3xwAAAAM/guy-punching-boom-punch.gif"]

fresko_img = ["https://i.ibb.co/sFt8Bhd/image.png", 
              "https://i.ibb.co/r7g56wn/image.png", 
              "https://i.ibb.co/HPjS9Q3/image.png", 
              "https://i.ibb.co/S3TcbXb/image.png",
              "https://i.ibb.co/GsYMrhJ/image.png", 
              "https://i.ibb.co/S74vXG2/image.png", 
              "https://i.ibb.co/m6cH5BZ/image.png",
              "https://i.ibb.co/CmTPQfx/image.png", 
              "https://i.ibb.co/LPjMgSL/image.png", 
              "https://i.ibb.co/J5pdjz0/image.png",
              "https://i.ibb.co/PYQLmyt/image.png",
              "https://i.ibb.co/9bVfD4g/image.png", 
              "https://i.ibb.co/X3qnMLq/image.png",
              "https://i.ibb.co/fXN3rG5/image.png", 
              "https://i.ibb.co/KFn6kF1/image.png",
              "https://i.ibb.co/HGhLdwt/image.png",
              "https://i.ibb.co/RcqbfXx/image.png",
              "https://i.ibb.co/G3bJbrj/image.png"]

hentai_img = ["https://i.ibb.co/Pr5rvbY/porno-komiks-gifki-seks-komiks-gifok-s-shikarnimi-2021-06-07-392132785-min.gif", 
              "https://i.ibb.co/rm3mNqM/Final-Fantasy-Porn-r34-Final-Fantasy-2907442-min.gif",
              "https://i.ibb.co/6DB0jkB/hent-min.gif", 
              "https://i.ibb.co/51CD8bq/Khentay-Gifki-Hentai-Gifs-18-amp-Animations-min-1.gif",
              "https://i.ibb.co/MGGXCT5/neko-hentai-nekopa-6504-min.gif",
              "https://i.ibb.co/fScrHLr/Tentay-Khentay-s-Tentaklyami-12-min.gif",
              "https://i.ibb.co/GCWVv7K/Hentaj-gif-Siski-anime-devushki-pokazyvajut-grud-12.gif", 
              "https://i.ibb.co/HTr1jTb/GTu-RHhy-YKs8.jpg",
              "https://i.ibb.co/bvhv8xt/d-Um2ik-Lq-XOA-819x1024.jpg",
              "https://i.ibb.co/d2GHxt0/no-Zaj3-Ojxb-Q.jpg",
              "https://i.ibb.co/0p7cX8Z/image.png",
              "https://i.ibb.co/mR4tYJ6/IMG-20220419-171019-822.jpg",
              "https://i.ibb.co/ccqvfJ4/image.png",
              "https://i.ibb.co/CvVJB7Q/image.png"]

meme_img = ["https://i.ibb.co/6sx3WPX/image.png",
            "https://i.ibb.co/f2RB1FQ/image.png",
            "https://i.ibb.co/gw5bpkL/image.png",
            "https://i.ibb.co/x3GGH0z/image.png",
            "https://i.ibb.co/vZvSyR8/image.png",
            "https://i.ibb.co/tCKcVDQ/image.png",
            "https://i.ibb.co/svSFJML/image.png",
            "https://i.ibb.co/Fww5xtb/image.png",
            "https://i.ibb.co/DpwrCBS/image.png",
            "https://i.ibb.co/YDGpQTW/image.png",
            "https://i.ibb.co/LnkLrh2/image.png",
            "https://i.ibb.co/DzyL2zT/image.png", 
            "https://i.ibb.co/rpjN3TF/image.png",
            "https://i.ibb.co/VpvKJ2J/image.png",
            "https://i.ibb.co/QCn8cyS/image.png",
            "https://i.ibb.co/nj7jS0q/image.png",
            "https://i.ibb.co/VQNGgrM/image.png",
            "https://i.ibb.co/W3xVS2v/image.png",
            "https://i.ibb.co/0BmLtwt/image.png",
            "https://i.ibb.co/61wsznq/image.png",
            "https://i.ibb.co/7p6Nk6n/image.png",
            "https://i.ibb.co/Pt9xMwk/image.png",
            "https://i.ibb.co/KNJ8mmF/image.png",
            "https://i.ibb.co/9W8zRnR/image.png",
            "https://i.ibb.co/WnN64kD/image.png",
            "https://i.ibb.co/hXhkYdz/image.png",
            "https://i.ibb.co/ZGh5JcC/image.png",
            "https://i.ibb.co/0Jp5cHB/image.png",
            "https://i.ibb.co/56DndRW/image.png",
            "https://i.ibb.co/KNQdLDk/image.png",
            "https://i.ibb.co/RjMfnsH/image.png",
            "https://i.ibb.co/LRtHpqJ/image.png",
            "https://i.ibb.co/JBkGnjF/image.png",
            "https://i.ibb.co/pwYn7L1/image.png",
            "https://i.ibb.co/kyD2V1p/image.png",
            "https://i.ibb.co/2FcFsrm/image.png",
            "https://i.ibb.co/PmVP8dV/image.png",
            "https://i.ibb.co/ZVzrnpZ/image.png",
            "https://i.ibb.co/nPHsPfL/image.png",
            "https://i.ibb.co/rGZKtfK/image.png",
            "https://i.ibb.co/t8Fmqrf/image.png",
            "https://i.ibb.co/JBYmP8C/image.png",
            "https://i.ibb.co/r79hqWs/image.png",
            "https://i.ibb.co/zZHHLKh/image.png",
            "https://i.ibb.co/ykQqkKc/image.png",
            "https://i.ibb.co/DwyCkVW/image.png",
            "https://i.ibb.co/sFkFY1m/image.png",
            "https://i.ibb.co/zVcCcWQ/image.png",
            "https://i.ibb.co/QpjLMy4/image.png",
            "https://i.ibb.co/n1nmpQL/image.png",
            "https://i.ibb.co/WVhn74n/image.png",
            "https://i.ibb.co/7SYcxfV/image.png",
            "https://i.ibb.co/C7cdFJf/image.png",
            "https://i.ibb.co/k5zRMd8/image.png",
            "https://i.ibb.co/bdNHr2C/image.png",
            "https://i.ibb.co/0F2v5vN/image.png",
            "https://i.ibb.co/X5Ms9v5/image.png",
            "https://i.ibb.co/1s9vp3k/image.png",
            "https://i.ibb.co/n10WmZj/image.png",
            "https://i.ibb.co/HLZWPxg/image.png",
            "https://i.ibb.co/JKvjC22/image.png",
            "https://i.ibb.co/68N45qk/image.png",
            "https://i.ibb.co/N3qts6v/image.png",
            "https://i.ibb.co/1TsLQ2P/image.png",
            "https://i.ibb.co/FDNB20K/image.png",
            "https://i.ibb.co/dJL46TZ/image.png",
            "https://i.ibb.co/WHcbpZ1/image.png",
            "https://i.ibb.co/f2c5C4q/image.png",
            "https://i.ibb.co/prDqrYv/image.png",
            "https://i.ibb.co/TMSg3sq/image.png",
            "https://i.ibb.co/dQYgz03/image.png",
            "https://i.ibb.co/YWcG8Nv/image.png",
            "https://i.ibb.co/jk9SGWV/image.png",
            "https://i.ibb.co/d68SC6H/image.png",
            "https://i.ibb.co/d68SC6H/image.png"]
            


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))





@client.event

async def on_ready():

    print("Bot is currently online!")
    await client.change_presence(status=discord.Status.online,activity=discord.Game(".help | v_0.0.1"))
    client.togetherControl = await DiscordTogether("OTY2NzYzNDc3OTYyMjE1NDg0.YmGepg.geLxkLCXC8PdMc3u4FR26mqVa40")


#help command

    @client.command(pass_context=True)

    async def help(ctx):

        author = ctx.send

        embed=discord.Embed(

            colour = discord.Colour.orange()
        )
        


        embed.set_author(name="Bot by Fikkich#0981", url="https://discord.gg/VhUDFAY7e3", icon_url="https://cdn.discordapp.com/attachments/896738147948445696/967534599121018960/Free_Sample_By_Wix.jpg")
        embed.add_field(name="Развлечения ", value="iq - проверить IQ🤔 \n hug - обнять пользователя🤗 \n kiss - поцеловать пользователя😘 \n punch - ударить пользователя👊 \n fresko - мемы с Жаком Фреско🤔 \n hentai - посмотреть хентай👁️ \n meme - случайные мемы🤣 \n eight_ball - задать вопрос боту❔", inline=False)
        embed.add_field(name="Монетка", value="coinflip - Подкинуть монетку🪙", inline=False)
        embed.add_field(name="Модерация", value="clear - Удалить сообщения🧹 \n kick - Кикнуть из сервера💥 \n ban - Забанить пользователя🚫", inline=False)
        embed.add_field(name="Лисичка", value="fox - увидеть лису🦊", inline=False)
        embed.add_field(name="Собака", value="dog - собака колобака🐕", inline=False)
        embed.add_field(name="Психологический возраст", value="age - узнать свой псих. возраст🧓", inline=False)
        embed.add_field(name="Ютуб", value="youtube - посмотреть ютуб с друзьями📺", inline=False)
        embed.add_field(name="Полезное", value="weather - Узнать погоду🌡️ \n user - информация про пользователя📒", inline=True)
        await ctx.send(embed=embed)
#IQ
@client.command(pass_context = True)
async def iq(ctx):
    embed = discord.Embed(title = "Ваш IQ ", description = (random.randint(1, 100)), color = (0xF85252))
    await ctx.send(embed = embed)




  
#Clear       
@client.command(name="очистить", aliases=["clear", "cls"], brief="Очистить чат от сообщений, по умолчанию 10.", usage="clear <amount=10>")
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Было удалено {amount + 1} уведомлений.", delete_after=3)




  
#MODERKA
@client.event
async def on_message(message):
    await client.process_commands(message)

    msg = message.content.lower()
    greeting_words = ["прив", "ку", "привет"]
    censored_words = ["даун", "давун", "конч", "кoнч", "чмоебота", "пидар","конченый"]

    if msg in greeting_words:
        await message.channel.send(f"{message.author.mention}, привет, как дела?")
    # 
    for bad_content in msg.split(" "):
        if bad_content in censored_words:
            await message.channel.send(f"{message.author.mention}, нельзя так говорить!")






          
#ПОГОДА
@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis: str = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Погода в 🌆 {city_name}",
                                  color=ctx.guild.me.top_role.color,
                                  timestamp=ctx.message.created_at, )
            embed.add_field(name="Описание", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура🌡️(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Влажность🚿(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Атмосферное давление💨(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Создано для {ctx.author.name}")
            await channel.send(embed=embed)
    elif not x["cod"] != "404":
            await channel.send("Город не найден🌆")
#Orel Reshka
@client.command()
async def coinflip(ctx):
    await ctx.send(random.choice(['Выпал - Орел🦅', 'Выпала - Решка🪙']))
  
#Лиса
@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Вот твоя лиса🦊') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
#Пес будеш майонез
@client.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Собака колобака🐕') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
#Псих
@client.command(pass_context = True)
async def age(ctx):
    embed = discord.Embed(title = "Ваш психологический возвраст🧓 ", description = (random.randint(15, 100)), color = (0x00B2F5))
    await ctx.send(embed = embed) #чуствую себя на 38 
#
@client.command()
async def youtube(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Нажми на ссылку, что бы зайти!\n{link}")

#
#авто выдача роли

@client.event

async def on_member_join (member):
    channel = client.get_channel ( 967873442911252490  )

    role = discord.utils.get (member.guild.roles, id = 967870858234310746)
    print ('user join the servers')
    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'``{member.name}`` присоединился к нам🙂', color = 0x0c0c0c))

#выдача 2
@client.event

async def on_member_join (member):
    channel = client.get_channel ( 896740746445594666  )

    role = discord.utils.get (member.guild.roles, id = 899039069319880724 )
    print ('user join the servers')
    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'``{member.name}`` присоединился к нам🙂', color = 0x0c0c0c))





  
#Кик
@client.command()
@commands.has_guild_permissions(manage_messages=True)
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.channel.send(f"{ctx.author.mention}, вы успешно кикнули пользователя!")
  
#Бан
@client.command()
@commands.has_guild_permissions(manage_messages=True)
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.channel.send(f"{ctx.author.mention}, вы успешно забанили пользователя!")      
#карточка
@client.command(name="user")
async def user(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"Информация про пользователя - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Создано для - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Ник:',value=user.display_name,inline=False)

    embed.add_field(name='Аккаунт создан:',value=user.created_at,inline=False)
    embed.add_field(name='Присоединился на сервер:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Является ботом?',value=user.bot,inline=False)

    embed.add_field(name=f'Список ролей: ({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Лучшая роль:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)
#Обнимашки
@client.command()
async def hug(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел обнять.")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} обнял {member.mention}")
    embed.set_image(url=f'{random.choice(img_hug)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#Полелуй
@client.command()
async def kiss(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел поцеловать")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} поцеловал {member.mention}")
    embed.set_image(url=f'{random.choice(img_kiss)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#фреско
@client.command()
async def fresko(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = ("Вот ваш фреско"))
        
    embed.set_image(url=f'{random.choice(fresko_img)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#ударить
@client.command()
async def punch(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ударить")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} ударил {member.mention}")
    embed.set_image(url=f'{random.choice(img_punch)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#хентай
@client.command()
async def hentai(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = ("Вот ваш хентайчик :)"))
        
    embed.set_image(url=f'{random.choice(hentai_img)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#мемы
@client.command()
async def meme(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = ("Вот твой мемчик :)"))
        
    embed.set_image(url=f'{random.choice(meme_img)}')#
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
#8бал
@client.command(name='8ball',
            description="Answers a yes/no question.",
            brief="Answers from the beyond.",
            aliases=['eight_ball', 'eightball', '8-ball'],
            pass_context=True)

async def eight_ball(context):
    possible_responses = [

        'ДА!!',
        'НЕТ!',
        'Хмм..Маловероятно',
        'Сложно ответить...',
        'Вполне возможно',
        'Определенно',
        'Может быть'

    ]
    await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)
#

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)