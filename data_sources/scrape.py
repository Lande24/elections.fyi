import asyncio
import pandas

from aiohttp import ClientSession
from html.parser import HTMLParser


async def main():
    async with ClientSession() as session:
        async with session.get("https://themadad.com/allpolls") as resp:
            if not resp.ok:
                print(f"Error: {resp.status}")
            html = await resp.text()
            
    tables = pandas.read_html(html)
    
    for i, table in enumerate(tables):
        table.to_csv(f"table{i}.csv")


if __name__ == "__main__":
    asyncio.run(main())
