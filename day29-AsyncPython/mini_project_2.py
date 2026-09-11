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