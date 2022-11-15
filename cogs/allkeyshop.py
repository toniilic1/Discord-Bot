import discord
from discord.ext import commands
from allkeys import AllKeySales


class ScrapeAllKeyShop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def allkeys(self, ctx, game):
        sales = AllKeySales.KeySales(game)
        i = 1
        embed = discord.Embed(
            title=f"{game} key sales on AllKeyShop",
            description="Check all key prices for the inputed game",
            color=discord.Colour.blurple()
        )
        for games in sales:
            embed.add_field(name=f"#{i}" ,value=("%s, **%s**" % games), inline=False)
            i+=1

        embed.set_author(name="Dev-Bot", icon_url="https://cdn-icons-png.flaticon.com/512/2021/2021646.png")
        embed.set_thumbnail(url="https://seeklogo.com/images/S/steam-logo-73274B19E3-seeklogo.com.png")
 
        await ctx.respond("Request proccesed.", embed=embed)

def setup(bot):
    bot.add_cog(ScrapeAllKeyShop(bot))
