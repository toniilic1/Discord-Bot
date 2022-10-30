import hikari
import lightbulb

plugin = lightbulb.Plugin('salekeys')
today = date.today()

@plugin.command
@lightbulb.command('keys', 'Which games are on sale?')
@lightbulb.implements(lightbulb.SlashCommand)
async def igkeys(ctx):
    await ctx.respond('')


def load(bot):
    bot.add_plugin(plugin)