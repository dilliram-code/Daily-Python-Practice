import asyncio
import random


# ============================================================
# 1. DOWNLOAD
# ============================================================

async def download_file(filename):
    print(f"[DOWNLOAD] {filename}: started")

    try:
        # Simulate network I/O.
        # In a real application this could be:
        #
        # await http_client.get(url)
        #
        await asyncio.sleep(random.uniform(1, 3))

        print(f"[DOWNLOAD] {filename}: finished")

        return f"{filename} data"

    except asyncio.CancelledError:
        print(f"[DOWNLOAD] {filename}: CANCELLED")

        # IMPORTANT:
        # We re-raise CancelledError so that cancellation
        # continues to propagate correctly.
        raise


# ============================================================
# 2. PROCESS
# ============================================================

async def process_file(filename, data):
    print(f"[PROCESS] {filename}: started")

    try:
        # Simulate processing.
        await asyncio.sleep(random.uniform(1, 3))

        print(f"[PROCESS] {filename}: finished")

        return f"processed {data}"

    except asyncio.CancelledError:
        print(f"[PROCESS] {filename}: CANCELLED")
        raise


# ============================================================
# 3. SAVE
# ============================================================

async def save_file(filename, processed_data):
    print(f"[SAVE] {filename}: started")

    try:
        # Simulate database/file I/O.
        await asyncio.sleep(random.uniform(1, 2))

        print(f"[SAVE] {filename}: finished")

    except asyncio.CancelledError:
        print(f"[SAVE] {filename}: CANCELLED")
        raise


# ============================================================
# 4. PROCESS ONE COMPLETE FILE
# ============================================================

async def process_job(filename):

    print(f"\n===== JOB {filename} STARTED =====")

    try:

        # Step 1: download
        data = await download_file(filename)

        # Step 2: process
        processed_data = await process_file(
            filename,
            data
        )

        # Step 3: save
        await save_file(
            filename,
            processed_data
        )

        print(f"===== JOB {filename} COMPLETED =====")

    except asyncio.CancelledError:

        print(f"===== JOB {filename} CANCELLED =====")

        # Re-raise cancellation.
        raise

    finally:

        # This block runs whether the job:
        #
        # - succeeds
        # - fails
        # - gets cancelled
        #
        print(f"[CLEANUP] {filename}: cleanup")


# ============================================================
# 5. MAIN JOB MANAGER
# ============================================================

async def main():

    filenames = [
        "file_A.csv",
        "file_B.csv",
        "file_C.csv"
    ]

    print("JOB MANAGER STARTED")

    try:

        # ----------------------------------------------------
        # TaskGroup creates a structured concurrency scope.
        # ----------------------------------------------------
        async with asyncio.TaskGroup() as tg:

            for filename in filenames:

                tg.create_task(
                    process_job(filename)
                )

        # We reach this point only when all child jobs
        # have completed successfully.
        print("\nALL JOBS COMPLETED")

    except* Exception as error:

        print("\nJOB MANAGER FAILED")
        print(error)

    finally:

        print("JOB MANAGER CLEANUP")
        print("JOB MANAGER FINISHED")


# ============================================================
# 6. PROGRAM ENTRY POINT
# ============================================================

asyncio.run(main())
