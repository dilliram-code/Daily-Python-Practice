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

async def fetch_attendance(): 
  
  print("Attendance API: started") 
  
  try: 
    
    await asyncio.sleep(5) 
    
    print("Attendance API: finished") 
    
    return 87 
  
  except asyncio.CancelledError: 
    
    print("Attendance API: CANCELLED") 
    
    raise


async def main(): 
  try: 
    async with asyncio.TaskGroup() as tg: 
      student_task = tg.create_task( fetch_student() ) 
      courses_task = tg.create_task( fetch_courses() ) 
      attendance_task = tg.create_task( fetch_attendance() ) 
  
  except* RuntimeError as error: 
    print("\nTaskGroup caught an error:") 
    print(error) 

asyncio.run(main())