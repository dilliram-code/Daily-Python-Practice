import asyncio

async def fetch_student():
  print("Student API: started")
  await asyncio.sleep(2)
  print("Student API: finished")
  return {
        "id": 101,
        "name": "Ram",
        "email": "ram@example.com"
    }

async def fetch_courses():
    print("Courses API: started")

    await asyncio.sleep(3)

    print("Courses API: finished")

    return [
        "Python",
        "Machine Learning",
        "Database"
    ]
