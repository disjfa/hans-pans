import discord
import os
import requests

client = discord.Client()

def get_dad_joke():
  response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'text/plain'})
  return response.text

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$haha'):
    joke = get_dad_joke();
    await message.channel.send(joke)
    return;

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    return;

client.run(os.getenv('APP_TOKEN'))
