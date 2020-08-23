import discord
import random
import string
import asyncio


token = "ur-token"




from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)


def random_phrase(length):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))


@client.command()
async def levelup(ctx,amount: int): # b'\xfc'
    await ctx.message.delete()
    msgsend = amount
    print(f"Sending {msgsend} messages\n\n")
    while msgsend > 0:
        msgsend -= 1
        print(f"Messages left to send: {msgsend}")
        rnd_out = random_phrase(5) + "-" + random_phrase(5) + " " + random_phrase(5) + "-" + random_phrase(5)
        await ctx.send(rnd_out)
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
        await asyncio.sleep(59)
    return



client.run(token, bot=False, reconnect=True)
