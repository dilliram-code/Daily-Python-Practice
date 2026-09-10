import asyncio 

async def worker(name):
  print(f"{name} started")
  await asyncio.sleep(5)
  print(f"{name} finished.")
  

async def main():
  asyncio.create_task(worker("Worker A"))
  asyncio.create_task(worker("Worker B"))
  asyncio.create_task(worker("Worker C"))
  
  print("Main finished.")


asyncio.run(main())