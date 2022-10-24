import lightbulb
import hikari
from tokens import token_id, guild_id

#must be granted bot, commands and administrator rights
bot = lightbulb.BotApp(
    token=token_id,
    default_enabled_guilds=(guild_id)#Register server with an ID so the commands are faster
)


@bot.command
@lightbulb.command('join', 'Makes bot join a voice channel')
@lightbulb.implements(lightbulb.PrefixCommand)
async def join(ctx):
    try:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.respond("I\'m in")
    except:
        await ctx.respond("You need to be connected to a voice channel in order for me to join")


@bot.command
@lightbulb.command('play', 'Plays track in connected voice channel')
@lightbulb.implements(lightbulb.PrefixCommand)
async def play(ctx, q: str):
    YDL_OPTIONS = {'default_search': 'auto', 'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = ctx.message.guild.voice_client
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(q, download=False)
            a = info['entries'][0]['formats'][0]['url']
            queue.append(a)
            if voice.is_playing():
                await ctx.respond('I have queued the track')
            else:
                idk = queue[0]
                queue.pop(0)
                voice.play(FFmpegPCMAudio(idk, **FFMPEG_OPTIONS))
        except:
            info = ydl.extract_info(q, download=False)
            a = info['url']
            queue.append(a)
            if voice.is_playing():
                await ctx.respond('I have queued the track')
            elif len(queue)==0:
                idk = queue[0]
                voice.play(FFmpegPCMAudio(idk, **FFMPEG_OPTIONS))
            else:
                idk = queue[0]
                queue.pop(0)
                voice.play(FFmpegPCMAudio(idk, **FFMPEG_OPTIONS))


bot.load_extensions('extensions.ping_pong', 'extensions.bot_info')
bot.run()