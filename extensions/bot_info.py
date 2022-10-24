import hikari
import lightbulb

plugin = lightbulb.Plugin('bot_info')

@plugin.command
@lightbulb.command('info', 'Get information about Odin')
@lightbulb.implements(lightbulb.SlashCommand)
async def info(ctx):
    await ctx.respond('Version: 0.1\nMade by: Toni\nAPIs used: Hikari and Lightbulb\nGithub links: https://github.com/hikari-py/hikari and https://github.com/hikari-py/hikari')


def load(bot):
    bot.add_plugin(plugin)