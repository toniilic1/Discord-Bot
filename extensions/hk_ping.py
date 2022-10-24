import hikari
import lightbulb

plugin = lightbulb.Plugin('hk_ping')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def ping(event):
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith("hk.ping"):
        await event.message.respond("Pong")

def load(bot):
    bot.add_plugin(plugin)