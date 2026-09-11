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

async def fetch_attendance():
    print("Attendance API: started")

    await asyncio.sleep(1)

    print("Attendance API: finished")

    return 87


# structured concurrency:

async def main():

    async with asyncio.TaskGroup() as tg:

        student_task = tg.create_task(
            fetch_student()
        )

        courses_task = tg.create_task(
            fetch_courses()
        )

        attendance_task = tg.create_task(
            fetch_attendance()
        )

    print(student_task.result())
    print(courses_task.result())
    print(attendance_task.result())

asyncio.run(main())