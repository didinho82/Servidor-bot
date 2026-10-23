import discord
import os

# Pega o token das variáveis de ambiente do Render (NUNCA coloque o token direto aqui)
TOKEN = os.getenv("DISCORD_TOKEN")

# Configura os intents (necessário para o bot funcionar)
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("Pong!")

# Inicia o bot
bot.run(TOKEN)
