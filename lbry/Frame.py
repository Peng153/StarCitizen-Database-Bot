import discord
from openpyxl import load_workbook

from openpyxl import load_workbook

load_wb = load_workbook("Data/Ship_Database.xlsx", data_only=True)
load_RSI = load_wb['RSI']

class ShipFrame:
    def __init__(self, title, footer, mft, name, image):
        self._title = title
        self._footer = footer
        self._MFT = mft
        self._name = name
        self._image = image
    
    def shipInfo(self):
        if(self._MFT == 'RSI' and self._name == 'ES'):
            _mft = load_RSI
            _num = 3

        if(self._MFT == 'RSI' and self._name == 'MR'):
            _mft = load_RSI
            _num = 4

        if(self._MFT == 'RSI' and self._name == 'CL'):
            _mft = load_RSI
            _num = 5
        
        if(self._MFT == 'RSI' and self._name == 'LN'):
            _mft = load_RSI
            _num = 6

        if(self._MFT == 'RSI' and self._name == 'LX'):
            _mft = load_RSI
            _num = 7
        

        embed = discord.Embed(
            title=(_mft.cell(_num,3-1).value), 
            description=(_mft.cell(_num,3+9).value), 
            colour = 00000000)
        embed.set_author(name= self._title)
        embed.add_field(name= "제조사", value=(_mft.cell(_num,3).value), inline= True)
        embed.add_field(name= "구현단계", value=(_mft.cell(_num,3+1).value), inline= False)
        embed.add_field(name= "전장/전폭/전고", value=(_mft.cell(_num,3+2).value), inline= True)
        embed.add_field(name= "최소/최대 승무원", value=(_mft.cell(_num,3+3).value), inline= True)
        embed.add_field(name= "순항/최대 속도", value=(_mft.cell(_num,3+4).value), inline= True)
        embed.add_field(name= "분류", value=(_mft.cell(_num,3+5).value), inline= True)
        embed.add_field(name= "출고중량", value=(_mft.cell(_num,3+6).value), inline= True)
        embed.add_field(name= "화물용적", value=(_mft.cell(_num,3+7).value), inline= True)
        embed.add_field(name= "가격($)", value=(_mft.cell(_num,3+8).value), inline= True)
        embed.set_image(url= self._image)
        embed.set_footer(text= self._footer)
        return embed
