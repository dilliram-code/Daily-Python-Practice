import asyncio 

async def fetch_student(): 
  
  print("Student API: started") 
  
  try: 
    
    await asyncio.sleep(5) 
    
    print("Student API: finished") 
    
    return { "id": 101, "name": "Ram" } 
  
  except asyncio.CancelledError: 
    
    print("Student API: CANCELLED") 
    
    raise

async def fetch_courses(): 
  
  print("Courses API: started") 
  
  await asyncio.sleep(1) 
  
  # Simulate an API failure 
  raise RuntimeError("Courses API failed!")