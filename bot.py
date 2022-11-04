import discord
from tokens import token_id
from igscrape import TrendingSales

bot = discord.Bot()
sales = TrendingSales.getTopTen()

@bot.event
async def on_ready():
    print(f"{bot.user} has risen from the dead")


@bot.command()
async def keys(ctx):
    i = 1
    embed = discord.Embed(
        title="Instant Gaming Sales",
        description="List of top ten most trending games on [Instant Gaming](https://www.instant-gaming.com/en/search/)",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )

    for games in sales:
        embed.add_field(name=f"#{i}" ,value=("*%s*, %s, **%s**" % games), inline=False)
        i+=1

    embed.set_author(name="Dev-Bot", icon_url="https://cdn-icons-png.flaticon.com/512/2021/2021646.png")
    embed.set_thumbnail(url="https://cdn.freebiesupply.com/logos/large/2x/instant-gaming-1-logo-png-transparent.png")
 
    await ctx.respond("Request proccesed.", embed=embed)


bot.run(token_id)