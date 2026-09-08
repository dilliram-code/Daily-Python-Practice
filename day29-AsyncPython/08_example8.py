import asyncio 

async def work(name):
  if name == "B":
    raise ValueError("Something went wrong.")
  
  await asyncio.sleep(2)
  
  print(name)
  

async def main():
  async with asyncio.TaskGroup() as tg:
    tg.create_task(work("A"))
    tg.create_task(work("B"))
    tg.create_task(work("C"))

asyncio.run(main())