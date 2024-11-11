import interactions
from interactions import OptionType

bot = interactions.Client(token="TOKEN_HERE", prefix="/")

@bot.command(
    name="hello",
    description="Say hello to the bot",
)
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command(
    name="greet",
    description="Greet a user",
    options=[
        interactions.Option(
            name="user",
            description="User to greet",
            type=OptionType.USER,
            required=True,
        )
    ],
)
async def greet(ctx, user):
    await ctx.send(f"Hello, {user.name}!")

@bot.event
async def on_ready():
    print('Bot is ready!')
bot.start()