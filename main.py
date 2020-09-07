import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

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
        embed = discord.Embed(
            title="도움말", 
            description="Roberts Space Industries 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "오로라ES", value="Auroraes, AuroraES, 오로라es, 오로라ES, 오로랃ㄴ, 오로라깡통", inline= False)
        embed.add_field(name= "오로라MR", value="Auroramr, AuroraMR, 오로라mr, 오로라MR, 오로라ㅡㄱ", inline= False)
        embed.add_field(name= "오로라CL", value="Auroracl, AuroraCL, 오로라cl, 오로라CL, 오로라치", inline= False)
        embed.add_field(name= "오로라LN", value="Auroraln, AuroraLN, 오로라ln, 오로라LN, 오로라ㅣㅜ", inline= False)
        embed.add_field(name= "오로라LX", value="Auroralx, AuroraLX, 오로라lx, 오로라LX, 오로라ㅣㅌ", inline= False)
        embed.set_author(name= _title)
        embed.set_footer(text= _footer)
        await context.send(embed=embed)

    # Help ANVL
    if name=="help_ANVL":
        embed = discord.Embed(
            title="도움말", 
            description="Anvil Aerospace 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "테스트", value="명령어 목록", inline= False)
        embed.set_author(name= _title)
        embed.set_footer(text= _footer)
        await context.send(embed=embed)

    # Help CRUS
    if name=="help_CRUS":
        embed = discord.Embed(
            title="도움말", 
            description="Crusader Industries 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "테스트", value="명령어 목록", inline= False)
        embed.set_author(name= _title)
        embed.set_footer(text= _footer)
        await context.send(embed=embed)

    # Aurora_ES
    if name=="Auroraes" or name=="AuroraES" or name=="오로라es" or name=="오로라ES" or name=="오로랃ㄴ" or name=="오로라깡통":
        _MFT = 'RSI'    # 제조사
        _name = 'ES'    # 기종
        _image = 'https://starcitizen.tools/images/8/8d/Aurora_ES_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
        await context.send(embed=embed)

    # Aurora_MR
    if name=="Auroramr" or name=="AuroraMR" or name=="오로라mr" or name=="오로라MR" or name=="오로라ㅡㄱ":
        _MFT = 'RSI'    # 제조사
        _name = 'MR'    # 기종
        _image = 'https://starcitizen.tools/images/c/c4/Aurora_MR_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
        await context.send(embed=embed)

    # Aurora_CL
    if name=="Auroracl" or name=="AuroraCL" or name=="오로라cl" or name=="오로라CL" or name=="오로라치":
        _MFT = 'RSI'    # 제조사
        _name = 'CL'    # 기종
        _image = 'https://starcitizen.tools/images/3/37/Aurora_CL_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
        await context.send(embed=embed)

    # Aurora_LN
    if name=="Auroraln" or name=="AuroraLN" or name=="오로라ln" or name=="오로라LN" or name=="오로라ㅣㅜ":
        _MFT = 'RSI'    # 제조사
        _name = 'LN'    # 기종
        _image = 'https://starcitizen.tools/images/6/6c/Aurora_LN_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
        await context.send(embed=embed)

    # Aurora_LX
    if name=="Auroralx" or name=="AuroraLX" or name=="오로라lx" or name=="오로라LX" or name=="오로라ㅣㅌ":
        _MFT = 'RSI'    # 제조사
        _name = 'LX'    # 기종
        _image = 'https://starcitizen.tools/images/9/94/Aurora_LX_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(_title, _footer, _MFT, _name, _image).shipInfo()
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