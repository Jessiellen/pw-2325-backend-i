import discord 
from discord.message import Message
from eticgpt.clients import OllamaAPI
from eticgpt.models import OllamaPrompt, OllamaResponse

intents= discord.Intents.default()

client = discord.Client(intentes=intents)
ollamaAPI=OllamaAPI()


@client.event
async def on_connect():
    print("I'm connecting...")

@client.event
async def on_ready():
    print('Connected!')

@client.event
async def on_menssage(message: Message):
    assert message


    if message.author != client.user:

        if message.content.startswith("/ask"):
            prompt=OllamaPrompt(
                prompt=message.content.split("/ask")[-1]
            )
            response: OllamaResponse= ollamaAPI.prompt(prompt=question)
            
            if not  response.done:
                await message.channel.send(":poop: oops!")

            else:
                await message.channel.send("response.response")

# client.run ()