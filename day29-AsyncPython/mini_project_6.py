import asyncio
import time

async def fetch_user_data(user_id: int):
    print(f"Start downloading user {user_id}...")
    # Simulate a network delay without blocking the thread
    await asyncio.sleep(2)
    print(f"Finished downloading user {user_id}!")
    return {"id": user_id, "status": "success"}

async def main():
    start_time = time.time()
    
    # Run 5 "downloads" concurrently
    user_ids = [1, 2, 3, 4, 5]
    results = await asyncio.gather(*(fetch_user_data(uid) for uid in user_ids))
    
    end_time = time.time()
    print(f"\nAll downloads complete in {end_time - start_time:.2f} seconds!")
    print("Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
