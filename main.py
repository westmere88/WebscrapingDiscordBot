from keep_alive import keep_alive
from DymocksWebScraping import getUserBook

import discord
import os

client = discord.Client()

#Returns the user choice so it can be used by DymocksWebScraping.py regardless of case, whitespace between '!' and the choice
def getBotFormattedChoice(choice):
    temp = choice.lower().replace("!", "", 1).lstrip()
    temp = '-'.join(temp.split())
    return temp



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!'):
    
    error_message="That's not an option. Check spelling or try getting any random book with '!book'"

    msg = getBotFormattedChoice(message.content)

    book = getUserBook(msg)
    if book == False:
      await message.channel.send(error_message) 

    else:
      await message.channel.send(book)  

def main():
  keep_alive()
  client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()