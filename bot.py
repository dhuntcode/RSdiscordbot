#      A Discord Bot to list active users during live shows on RadioSEGA
#      Written by INeedFruit©TM opensource.init 2020

import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

rundownBot = commands.Bot(command_prefix = '!')

#lists to store the names of active users. Number represent the number of hours before list is cleared.
activeMembers1 = []
activeMembers2 = []
activeMembers3 = []

@rundownBot.event # function to show the bot is ready and to start the task loop
async def on_ready():
    clearList1.start()
    clearList2.start()
    clearList3.start()
    print('Bot is ready')

@rundownBot.event    #main function for storing user names in the list
async def on_message(message):
    if message.author.name not in activeMembers1:
      activeMembers1.append(message.author.name)
      #print('Active user list 1 hour updated')
    if message.author.name not in activeMembers2:
      activeMembers2.append(message.author.name)
      #print('Active user list 2 hour updated')
    if message.author.name not in activeMembers3:
      activeMembers3.append(message.author.name)
      #print('Active user list 3 hour updated')
    await rundownBot.process_commands(message)
from discord.ext.commands import CommandNotFound

@rundownBot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@rundownBot.command(hidden=True)    #the three commands for DM'ing the list of users.
async def rundown1(message):
    await message.author.send(activeMembers1)
@rundownBot.command(hidden=True)
async def rundown2(message):
    await message.author.send(activeMembers2)
@rundownBot.command(hidden=True)
async def rundown3(message):
    await message.author.send(activeMembers3)

@tasks.loop(hours=1)     #three loops to clear the lists of names on specific hours
async def clearList1():
  activeMembers1.clear()
  #print('Active user list 1 hour cleared')

@tasks.loop(hours=2)
async def clearList2():
  activeMembers2.clear()
  #print('Active user list 2 hour cleared')

@tasks.loop(hours=3)
async def clearList3():
  activeMembers3.clear()
  #print('Active user list 3 hour cleared')

rundownBot.run(token)
