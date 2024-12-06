import discord
from dotenv import load_dotenv
import os

load_dotenv()
botToken = os.getenv("token")

class myClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents=intents)
client.run(botToken)

