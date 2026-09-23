import asyncio

async def check_status(name: str, delay: int):
  print(f"[{name}] start checking...")
  await asyncio.sleep(delay)
  print(f"Finished [{name}] after {delay} seconds...")
  return f"{name}: Success!"