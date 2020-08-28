import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

from openpyxl import load_workbook

from lbry.Frame import ShipFrame

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

# 토큰 입력
token = "NzEwMzUxNDQyOTUwNzUwMjgx.XrzMVQ.etzGv5bLbLBTK5BRcUE2Yi59nVk"


@bot.event
async def on_ready():

    #봇의 아이디, 닉네임 표시
    print("==============")
    print("봇이 실행 중...")
    print(bot.user.name)
    print(bot.user.id)
    print("==============")
    
    #봇 상태 출력
    activity = discord.Game(name="!help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)


_title = '스타시티즌 DB 봇'
_footer = "A/S 문의 Peng#8377"


@bot.command()  # 도움말
async def help(context):
    embed = discord.Embed(
            title="도움말 페이지", 
            description="이 봇은 SCDB로서 다음과 같은 명령어를 가집니다.", 
            colour = 00000000)
    embed.set_author(name= _title)
    embed.set_footer(text= _footer)
    await context.send(embed=embed)


@bot.command()  # 함선정보
async def ship(context, name=None):
    # None
    if name==None:
        embed = discord.Embed(
            title="도움말", 
            description="!ship 함선이름 으로 입력해주세요.", 
            colour = 00000000)
        embed.set_author(name= self.title)
        embed.set_footer(text= self.footer)
        await context.send(embed=embed)

    # Aurora_ES
    if name=="오로라ES" or name=="오로라es" or name=="오로라깡통":
        _MFT = 'RSI'    # 제조사
        _name = 'ES'    # 기종
        _image = 'https://starcitizen.tools/images/thumb/d/d0/Aurora_ES_in_black_room_-_Isometric.png/900px-Aurora_ES_in_black_room_-_Isometric.png'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
        await context.send(embed=embed)

    # Aurora_MR
    if name=="오로라MR" or name=="오로라mr":
        # <<
        await context.send(embed=embed)

    # Aurora_CL
    if name=="오로라CL" or name=="오로라cl":
        # <<
        await context.send(embed=embed)

    # Aurora_LN
    if name=="오로라LN" or name=="오로라ln":
        # <<
        await context.send(embed=embed)

    # Aurora_LX
    if name=="오로라LX" or name=="오로라lx":
        # <<
        await context.send(embed=embed)

    # Arrow
    if name=="애로우" or name=="애로롱":
        embed = discord.Embed(
            title="함선 이름", 
            description="함선 설명", 
            colour = 00000000)
        embed.set_author(name= '스타시티즌 DB 봇')
        embed.add_field(name= "분류", value= 'r', inline= False)
        embed.add_field(name= "전장/전폭/전고", value= 'r', inline= True)
        embed.add_field(name= "최소/최대 승무원", value= 'r', inline= True)
        embed.add_field(name= "순항/최대 속도", value= 'r', inline= True)
        embed.add_field(name= "구현단계", value= 'r', inline= True)
        embed.add_field(name= "출고중량", value= 'r', inline= True)
        embed.add_field(name= "화물용적", value= 'r', inline= True)
        embed.add_field(name= "가격", value= 'r', inline= True)
        embed.set_image(url= '')
        embed.set_footer(text= "A/S 문의 Peng#8377")
        await context.send(embed=embed)

        

    

bot.run(token)