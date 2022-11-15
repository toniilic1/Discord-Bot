import discord
from tokens import token_id # make a python file named tokens.py and a variable inside it containing your bot id

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} has risen from the dead")



cogs_list = [
    'instantgaming',
    'allkeyshop'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(token_id) # bot token