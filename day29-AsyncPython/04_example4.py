import asyncio 
import time 

async def work(name):
  
  print(f"{name} started")
  await asyncio.sleep(2)
  print(f"{name} finished")

async def main():
  
  task1 = asyncio.create_task(work("A"))
  task2 = asyncio.create_task(work("B"))
  task3 = asyncio.create_task(work("C"))
  
  await task1 
  await task2 
  await task3 

asyncio.run(main())