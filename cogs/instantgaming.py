import discord
from discord.ext import commands
from igscrape import TrendingSales


class ScrapeGaming(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def keys(self, ctx):
        sales = TrendingSales.getTopTen()
        i = 1
        embed = discord.Embed(
            title="Instant Gaming Sales",
            description="List of top ten most trending games on [Instant Gaming](https://www.instant-gaming.com/en/search/)",
            color=discord.Colour.blurple()
        )
        for games in sales:
            embed.add_field(name=f"#{i}" ,value=("*%s*, %s, **%s**" % games), inline=False)
            i+=1

        embed.set_author(name="Dev-Bot", icon_url="https://cdn-icons-png.flaticon.com/512/2021/2021646.png")
        embed.set_thumbnail(url="https://cdn.freebiesupply.com/logos/large/2x/instant-gaming-1-logo-png-transparent.png")
 
        await ctx.respond("Request proccesed.", embed=embed)

def setup(bot):
    bot.add_cog(ScrapeGaming(bot))
