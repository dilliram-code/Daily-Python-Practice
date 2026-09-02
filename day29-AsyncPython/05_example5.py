import asyncio 

async def work(name):
  await asyncio.sleep(2)
  return f"{name} finished"

async def main():
  results = await asyncio.gather(
    work("A"),
    work("B"),
    work("C")
  )
  print(results)

asyncio.run(main())