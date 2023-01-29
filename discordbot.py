import os
import discord
from dotenv import load_dotenv
import asyncio
from random import randrange
import yfinance as yf
from wallstreet import Stock

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	#print("Setting initial description")
    await client.change_presence (activity = discord.Activity(type=discord.ActivityType.watching, name="TestTEst"))
    print("Finished onready function")
    await updatePrice()

@client.event
async def updatePrice():
	print("Checking client is not closed")
	while not client.is_closed():
		print("Beginning description change")

		SNP500 = Stock('SPY')
		SNP500Price = SNP500.price 
		SNP500Change = round(SNP500.change, 3)

		print(SNP500Price)
		print(SNP500Change)

		UpdatedDescription = ""

		if SNP500Change > 0:
			UpdatedDescription = str(SNP500Price) + " " + '\u2191' + " " + str(SNP500Change) + "%"
		elif SNP500Change < 0:
			UpdatedDescription = str(SNP500Price) + " " + '\u2193' + " " + str(SNP500Change) + "%"
		else:
			UpdatedDescription = str(SNP500Price) + " " + "=" + " " + str(SNP500Change) + "%"

		print(UpdatedDescription)

		await client.change_presence (activity = discord.Activity(type=discord.ActivityType.watching, name=UpdatedDescription))
		print("Sleeping before next description change")
		await asyncio.sleep(5)

async def main():
	async with client:
		await client.start(TOKEN)
		await client.on_ready()

asyncio.run(main())

class 