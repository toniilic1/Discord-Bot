import discord
from discord.ext import commands
from steamscrape import TrendingSales


class ScrapeSteam(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def charts(self, ctx):
        sales = TrendingSales.getTopTen()
        i = 1
        embed = discord.Embed(
            title="Steam New Trending",
            description="List of top ten most trending NEW games on [Steam](https://store.steampowered.com/explore/new/)",
            color=discord.Colour.blurple()
        )
        for games in sales:
            embed.add_field(name=f"#{i}" ,value=("%s, **%s**" % games), inline=False)
            i+=1

        embed.set_author(name="Dev-Bot", icon_url="https://cdn-icons-png.flaticon.com/512/2021/2021646.png")
        embed.set_thumbnail(url="https://seeklogo.com/images/S/steam-logo-73274B19E3-seeklogo.com.png")
 
        await ctx.respond("Request proccesed.", embed=embed)

def setup(bot):
    bot.add_cog(ScrapeSteam(bot))
