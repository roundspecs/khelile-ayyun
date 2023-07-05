import os
from math import log2

from discord import (
    Activity,
    ActivityType,
    ApplicationContext,
    Bot,
    Embed,
    Intents,
    Member,
    Option,
    Status,
)
from discord.ext.commands import has_permissions
from dotenv import load_dotenv

from constants import ABOUT_DESCRIPTION, ABOUT_FOOTER, ABOUT_TITLE, PRIMARY_COLOR

# path of this file
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# load all the variables from the env file
load_dotenv(os.path.join(BASEDIR, ".env-var"))

# initialize the bot
bot = Bot(
    intents=Intents.all(),
    activity=Activity(type=ActivityType.playing, name="Duel against Tourist"),
    status=Status.do_not_disturb,
)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(
    name="handle_set", description="Register/change your codeforces handle"
)
async def handle_set(
    ctx: ApplicationContext,
    handle: Option(input_type=str, description="Codeforces handle", required=True),
    member: Option(Member, description="Member of this server"),
):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="whois", description="Play duel against an opponent")
async def whois(
    ctx: ApplicationContext, member: Option(Member, description="Member of this server")
):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="duel", description="Play duel against an opponent")
async def duel(
    ctx: ApplicationContext,
    opponent: Option(Member, description="Member of this server"),
    rating: Option(int, description="Rating of problem"),
):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="duel_withdraw", description="Play duel against an opponent")
async def duel_witdraw(ctx: ApplicationContext):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(
    name="tournament_cancel", description="Cancel the current tournament"
)
@has_permissions(moderate_members=True)
async def tournament_withdraw(ctx: ApplicationContext):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="tournament_create", description="Create a new tournament")
@has_permissions(moderate_members=True)
async def tournament_create(
    ctx: ApplicationContext,
    n: Option(input_type=int, description="Number of players", required=True),
):
    # verification
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = (
        "Number of players should be\n"
        ":point_right: an integer\n"
        ":point_right: a power of 2\n"
        ":point_right: between [8,128]"
    )
    if not n.isdecimal():
        await ctx.respond(embed=embed, ephemeral=True)
        return
    n = log2(int(n))
    if not (n.is_integer() and 3 <= n <= 7):
        await ctx.respond(embed=embed, ephemeral=True)
        return

    # TODO
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="about", description="Get to know খেলিলি আইয়ুন")
async def about(ctx: ApplicationContext):
    embed = Embed(
        title=ABOUT_TITLE,
        description=ABOUT_DESCRIPTION,
        color=PRIMARY_COLOR,
    )
    embed.set_footer(text=ABOUT_FOOTER)
    await ctx.respond(embed=embed, ephemeral=True)


bot.run(os.getenv("TOKEN"))  # run the bot with the token
