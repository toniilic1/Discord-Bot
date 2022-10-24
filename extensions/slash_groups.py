import hikari
import lightbulb

plugin = lightbulb.Plugin('slash_groups')

@plugin.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def odin_group(ctx):
    pass

@odin_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def odin_subcommand(ctx):
    await ctx.respond('Im a subcommand')

@plugin.command
@lightbulb.option('num2', 'second number', type=int)
@lightbulb.option('num1', 'first number', type=int) #must be above add command
@lightbulb.command('add', "add two numbers together")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

def load(bot):
    bot.add_plugin(plugin)