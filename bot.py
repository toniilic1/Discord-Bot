import lightbulb  # development branch 
import hikari
from tokens import token_id, guild_id

#must be granted bot, commands and administrator rights
# use token id and guild id of your server for privacy
bot = lightbulb.BotApp(
    token=token_id,
    default_enabled_guilds=(guild_id)#Register server with an ID so the commands are faster
)


bot.load_extensions('extensions.ping_pong', 'extensions.bot_info')
bot.run()