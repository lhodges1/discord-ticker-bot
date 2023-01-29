import os
import discord
from dotenv import load_dotenv
import asyncio
from random import randrange
import yfinance as yf
from wallstreet import Stock
from bot.py import Bot

class InitialiseBot:
	def __init__(self):
		load_dotenv()

		tickers = []
		with open(r"tickers.txt") as fp:
			for count, line in enumerate(fp):
				pass

		tickerCount = count + 1

		client = discord.Client(intents=discord.Intents.default())

		botList = []

		for x in range(tickerCount):
			token = os.getenv(str(x+1))
			print(token)
			Bot(token, )


InitialiseBot()




