import hikari
import lightbulb

plugin = lightbulb.Plugin('msg_terminal')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

def load(bot):
    bot.add_plugin(plugin)