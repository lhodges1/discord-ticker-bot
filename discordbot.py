import os
import discord
from dotenv import load_dotenv
import asyncio
from random import randrange
import yfinance as yf

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
		SNP500 = str(round(yf.Ticker("SPY").fast_info['last_price'], 3))
		print(SNP500)
		await client.change_presence (activity = discord.Activity(type=discord.ActivityType.watching, name="Price: " + SNP500))
		print("Sleeping before next description change")
		await asyncio.sleep(30)

async def main():
	async with client:
		await client.start(TOKEN)
		await client.on_ready()

asyncio.run(main())