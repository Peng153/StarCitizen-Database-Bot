import discord

from openpyxl import load_workbook
from lbry.Frame import ShipFrame

load_wb = load_workbook("Data/Ship_Database.xlsx", data_only=True)
load_RSI = load_wb['RSI']

_title = '스타시티즌 DB 봇'
_footer = "A/S 문의 Peng#8377"

class RSI:
    def __init__(self, title, footer):
        self._Title = title
        self._Footer = footer

    def Help_RSI(self):
        embed = discord.Embed(
            title="도움말", 
            description="Roberts Space Industries 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "오로라ES", value="Auroraes, AuroraES, 오로라es, 오로라ES", inline= False)
        embed.add_field(name= "오로라MR", value="Auroramr, AuroraMR, 오로라mr, 오로라MR", inline= False)
        embed.add_field(name= "오로라CL", value="Auroracl, AuroraCL, 오로라cl, 오로라CL", inline= False)
        embed.add_field(name= "오로라LN", value="Auroraln, AuroraLN, 오로라ln, 오로라LN", inline= False)
        embed.add_field(name= "오로라LX", value="Auroralx, AuroraLX, 오로라lx, 오로라LX", inline= False)
        embed.set_author(name= self._Title)
        embed.set_footer(text= self._Footer)

        return embed
        
    def Aurora_ES(self):
        _MFT = load_RSI   # 제조사
        _num = 3
        _image = 'https://starcitizen.tools/images/8/8d/Aurora_ES_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Aurora_MR(self):
        _MFT = load_RSI    # 제조사
        _num = 4
        _image = 'https://starcitizen.tools/images/c/c4/Aurora_MR_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Aurora_CL(self):
        _MFT = load_RSI    # 제조사
        _num = 5
        _image = 'https://starcitizen.tools/images/8/8d/Aurora_CL_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Aurora_LN(self):
        _MFT = load_RSI    # 제조사
        _num = 6
        _image = 'https://starcitizen.tools/images/6/6c/Aurora_LN_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Aurora_LX(self):
        _MFT = load_RSI    # 제조사
        _num = 7
        _image = 'https://starcitizen.tools/images/9/94/Aurora_LX_in_SelfLand_-_Isometric.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Apollo_Tri(self):
        _MFT = load_RSI    # 제조사
        _num = 9
        _image = 'https://starcitizen.tools/images/b/b5/Apollo_Landed_Concept.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Apollo_Med(self):
        _MFT = load_RSI    # 제조사
        _num = 10
        _image = 'https://starcitizen.tools/images/8/89/Medivac_-_Under_attack_above_world_while_rescuing_with_drone_-_Rear_Starboard.jpg'

        embed = ShipFrame(self._Title, self._Footer, _MFT, _num, _image).shipInfo()
        return embed

    def Constellation(self):
        return

    def Other_RSI(self):
        return



class ANVL:
    def __init__(self, title, footer):
        self._Title = title
        self._Footer = footer

    def Help_ANVL(self):
        embed = discord.Embed(
            title="도움말", 
            description="Anvil Aerospace 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "테스트", value="명령어 목록", inline= False)
        embed.set_author(name= self._Title)
        embed.set_footer(text= self._Footer)

        return embed



class CRUS:
    def __init__(self, title, footer):
        self._Title = title
        self._Footer = footer

    def Help_CRUS(self):
        embed = discord.Embed(
            title="도움말", 
            description="Crusader Industries 항목의 명령어 목록입니다. 대문자와 띄어쓰기에 주의 해 주시길 바랍니다.", 
            colour = 00000000)
        embed.add_field(name= "테스트", value="명령어 목록", inline= False)
        embed.set_author(name= self._Title)
        embed.set_footer(text= self._Footer)

        return embed