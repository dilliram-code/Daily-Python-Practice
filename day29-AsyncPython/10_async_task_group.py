import asyncio


async def task_a():
    await asyncio.sleep(2)
    print("Task A finished")


async def task_b():
    await asyncio.sleep(1)
    print("Task B finished")


async def task_c():
    await asyncio.sleep(3)
    print("Task C finished")


async def main():

    async with asyncio.TaskGroup() as group:

        group.create_task(task_a())
        group.create_task(task_b())
        group.create_task(task_c())

    print("All tasks finished")


asyncio.run(main())