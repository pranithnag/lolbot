import discord
import random
import datetime
from discord.ext import commands

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['pfp', 'av', 'prfp'])
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        
        show_avatar = discord.Embed(
            description="[Avatar URL](%s)" % member.avatar_url,
            timestamp=datetime.datetime.utcnow(),
            color=random.randint(0, 0xFFFFFF))
        show_avatar.set_image(url=f"{member.avatar_url}")
        show_avatar.set_footer(text=f'{member}')
        await ctx.send(embed=show_avatar)

def setup(bot):
    bot.add_cog(image(bot))