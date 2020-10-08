import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

from lbry.Frame import ShipFrame
from lbry.Ship import RSI, ANVL, CRUS

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

# 토큰 입력
token = ""


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
    embed.add_field(name= "함선정보 명령어", value="!ship help", inline= True)
    embed.set_author(name= _title)
    embed.set_footer(text= _footer)
    await context.send(embed=embed)


@bot.command()  # 함선정보
async def ship(context, name=None):
    # None
    if name==None:
        embed = discord.Embed(
            title="도움말", 
            description="!ship \"함선이름\" 으로 입력해주세요.\n 명령어는 !ship help를 입력하여 참조해주시길 바랍니다.", 
            colour = 00000000)
        embed.set_author(name= _title)
        embed.set_footer(text= _footer)
        await context.send(embed=embed)

    # Help
    if name=="help":
        embed = discord.Embed(
            title="도움말", 
            description="!ship의 부속 명령어는 다음 명령어를 참조해주십시오.", 
            colour = 00000000)
        embed.add_field(name= "Roberts Space Industries", value="help_RSI", inline= True)
        embed.add_field(name= "Anvil Aerospace", value="help_ANVL", inline= True)
        embed.add_field(name= "Crusader Industries", value="help_CRUS", inline= True)
        embed.set_author(name= _title)
        embed.set_footer(text= _footer)
        await context.send(embed=embed)



    # Help RSI
    if name=="help_RSI":
        embed = RSI(_title, _footer).Help_RSI() # lbry/Ship -> RSI Class -> Help_RSI
        await context.send(embed=embed)

    # Help ANVL
    if name=="help_ANVL":
        embed = ANVL(_title, _footer).Help_ANVL() # lbry/Ship -> ANVL Class -> Help_ANVL
        await context.send(embed=embed)

    # Help CRUS
    if name=="help_CRUS":
        embed = CRUS(_title, _footer).Help_CRUS() # lbry/Ship -> CRUS Class -> Help_CRUS
        await context.send(embed=embed)



    # Aurora_ES
    if name=="Auroraes" or name=="AuroraES" or name=="오로라es" or name=="오로라ES" or name=="오로랃ㄴ" or name=="오로라깡통":
        embed = RSI(_title, _footer).Aurora_ES() # lbry/Ship -> RSI Class -> Aurora_ES
        await context.send(embed=embed)

    # Aurora_MR
    if name=="Auroramr" or name=="AuroraMR" or name=="오로라mr" or name=="오로라MR" or name=="오로라ㅡㄱ":
        embed = RSI(_title, _footer).Aurora_MR() # lbry/Ship -> RSI Class -> Aurora_MR
        await context.send(embed=embed)

    # Aurora_CL
    if name=="Auroracl" or name=="AuroraCL" or name=="오로라cl" or name=="오로라CL" or name=="오로라치":
        embed = RSI(_title, _footer).Aurora_CL() # lbry/Ship -> RSI Class -> Aurora_CL
        await context.send(embed=embed)

    # Aurora_LN
    if name=="Auroraln" or name=="AuroraLN" or name=="오로라ln" or name=="오로라LN" or name=="오로라ㅣㅜ":
        embed = RSI(_title, _footer).Aurora_LN() # lbry/Ship -> RSI Class -> Aurora_LN
        await context.send(embed=embed)

    # Aurora_LX
    if name=="Auroralx" or name=="AuroraLX" or name=="오로라lx" or name=="오로라LX" or name=="오로라ㅣㅌ":
        embed = RSI(_title, _footer).Aurora_LX() # lbry/Ship -> RSI Class -> Aurora_LX
        await context.send(embed=embed)

    # Apollo Triage
    if name=="Apollotriage" or name=="ApolloTriage" or name=="아폴로트리아지" or name=="빨간아폴로" or name=="붉은병원선":
        embed = RSI(_title, _footer).Apollo_Tri() # lbry/Ship -> RSI Class -> Apollo_Tri
        await context.send(embed=embed)

    # Apollo Medivac
    if name=="Apollomedivac" or name=="ApolloMedivac" or name=="아폴로메디벡" or name=="흰아폴로" or name=="하얀병원선":
        embed = RSI(_title, _footer).Apollo_Med() # lbry/Ship -> RSI Class -> Apollo_Med
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