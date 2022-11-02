import discord
from tokens import token_id

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} has risen from the dead")

@bot.slash_command(name = 'hello', description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(token_id)