import asyncio 

async def work(name, delay):
  await asyncio.sleep(delay)
  return name 

async def main():
  results = await asyncio.gather(
  work("A", 3),
  work("B", 2),
  work("C", 1)
)
  print(results)

asyncio.run(main())

