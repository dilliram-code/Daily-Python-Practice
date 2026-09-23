import asyncio

async def check_status(name: str, delay: int):
  print(f"[{name}] start checking...")
  await asyncio.sleep(delay)
  print(f"Finished [{name}] after {delay} seconds...")
  return f"{name}: Success!"

async def main():
  
  """Starting all coroutines concurrently"""
  results = await asyncio.gather(
    check_status("Server-Alpha", 2),
    check_status("Database-Beta", 3),
    check_status("Cache-Gamma", 1)
  )
  
  print("All checks completed!")
  print("Results: ", results)
  
if __name__ == "__main__":
  asyncio.run(main())