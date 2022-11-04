import discord
from tokens import token_id
from igscrape import TrendingSales

bot = discord.Bot()
sales = TrendingSales.getTopTen()
str(sales)

@bot.event
async def on_ready():
    print(f"{bot.user} has risen from the dead")

#@bot.slash_command(name = 'keys', description = "get trending instant gaming sales")
#async def keys(ctx):
 #   await ctx.respond(str(sales[0][0]))

@bot.command()
async def keys(ctx):
    embed = discord.Embed(
        title="Instant Gaming Sales",
        description="List of top ten most trending games on Instant Gaming",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    #embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

    for i in range(0,7):
        embed.add_field(name="%" ,value=sales[i][0], inline=True)
        embed.add_field(name="Game Name", value=sales[i][1], inline=True)
        embed.add_field(name="Price", value=sales[i][2], inline=True)


    embed.set_author(name="Dev-Bot", icon_url="https://cdn-icons-png.flaticon.com/512/2021/2021646.png")
    embed.set_thumbnail(url="https://cdn.freebiesupply.com/logos/large/2x/instant-gaming-1-logo-png-transparent.png")
    #embed.set_image(url="https://example.com/link-to-my-banner.png")
 
    await ctx.respond("Request proccesed.", embed=embed)


bot.run(token_id)