import discord
from tokens import token_id
from igscrape import TrendingSales

bot = discord.Bot()
sales = TrendingSales

@bot.event
async def on_ready():
    print(f"{bot.user} has risen from the dead")

@bot.slash_command(name = 'keys', description = "get trending instant gaming sales")
async def keys(ctx):
    await ctx.respond(str(sales.getTopTwenty()))

bot.run(token_id)