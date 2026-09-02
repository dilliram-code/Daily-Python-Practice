import asyncio
import time 

async def work(name):
  
  print(f"{name} started")
  await asyncio.sleep(5)
  print(f"{name} finished")

async def main():
  await work("A")
  await work("B")
  await work("C")

asyncio.run(main())