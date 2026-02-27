# test-priya.py
from dotenv import load_dotenv
import os

##load_dotenv()                      # looks for .env in cwd
# – or load_dotenv("../.env") if you run from a subdirectory

print(os.getenv("TAVILY_API_KEY"))
import os
import asyncio
from tavily import AsyncTavilyClient

print("KEY SET?", bool(os.getenv("TAVILY_API_KEY")))


async def main():
	client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
	res = await client.search("what is AI", max_results=1)
	print(res)


asyncio.run(main())