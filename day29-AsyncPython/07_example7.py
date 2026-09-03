import asyncio 

async def work(name):
  await asyncio.sleep(2)
  print(f"{name} finished")
  

async def main():
  async with asyncio.TaskGroup() as tg:
    tg.create_task(work("A"))
    tg.create_task(work("B"))
    tg.create_task(work("C"))
    
asyncio.run(main())