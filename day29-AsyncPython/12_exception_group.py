import asyncio

async def task_a():
    raise ValueError("Invalid value")

async def task_b():
    raise TypeError("Wrong type")
  
async def main():
  
  try:
    
    async with asyncio.TaskGroup as group:
      group.create_task(task_a())
      group.create_task(task_b())
      
  except* ValueError:
    print("ValueError handled.")
  
  except* TypeError:
    print("TypeError handled.")

asyncio.run(main())