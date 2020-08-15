import discord


class ShipFrame:
    def __init__(self, title, footer):
        self._title = title
        self._footer = footer
    
    def shipInfo(self):
        embed = discord.Embed(
            title="함선 이름", 
            description="함선 설명", 
            colour = 00000000)
        embed.set_author(name= self._title)
        embed.add_field(name= "분류", value= 'r', inline= False)
        embed.add_field(name= "전장/전폭/전고", value= 'r', inline= True)
        embed.add_field(name= "최소/최대 승무원", value= 'r', inline= True)
        embed.add_field(name= "순항/최대 속도", value= 'r', inline= True)
        embed.add_field(name= "구현단계", value= 'r', inline= True)
        embed.add_field(name= "출고중량", value= 'r', inline= True)
        embed.add_field(name= "화물용적", value= 'r', inline= True)
        embed.add_field(name= "가격", value= 'r', inline= True)
        embed.set_image(url= '')
        embed.set_footer(text= self._footer)
        return embed
