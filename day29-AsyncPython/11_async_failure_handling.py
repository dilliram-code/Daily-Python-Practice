import asyncio 

async def task_a():
    await asyncio.sleep(1)
    print("A finished")


async def task_b():
    await asyncio.sleep(2)
    raise ValueError("Something went wrong in B")


async def task_c():
    await asyncio.sleep(5)
    print("C finished")
    
async def main():

    async with asyncio.TaskGroup() as group:
        group.create_task(task_a())
        group.create_task(task_b())
        group.create_task(task_c())

asyncio.run(main())