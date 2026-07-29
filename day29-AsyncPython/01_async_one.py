import asyncio

async def hello():
  print("Hello")
  await asyncio.sleep(5)
  print("Dilli")
asyncio.run(hello())