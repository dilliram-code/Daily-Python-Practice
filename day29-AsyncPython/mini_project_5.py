import asyncio
import time
import aiohttp

# Define a list of URLs to check concurrently
URLS = [
    "https://httpbin.org",
    "https://httpbin.org",
    "https://httpbin.org",  # Will take ~2 seconds
    "https://httpbin.org",
    "https://invalid-url-that-will-fail.xyz"
]

async def check_url(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetches a URL asynchronously and returns its status or error."""
    start_time = time.time()
    try:
        # Enforce a 3-second timeout per request so slow sites don't stall the system
        async with session.get(url, timeout=3.0) as response:
            latency = time.time() - start_time
            print(f"✅ Fetched {url} in {latency:.2f}s")
            return {"url": url, "status": response.status, "latency": latency, "error": None}
            
    except asyncio.TimeoutError:
        print(f"⏳ Timeout checking {url}")
        return {"url": url, "status": None, "latency": None, "error": "Timeout"}
    except Exception as e:
        print(f"❌ Failed checking {url}: {type(e).__name__}")
        return {"url": url, "status": None, "latency": None, "error": type(e).__name__}

async def main():
    print(f"Starting status checks on {len(URLS)} URLs...")
    start_total = time.time()

    # Reuse a single ClientSession for optimal connection pooling
    async with aiohttp.ClientSession() as session:
        # 1. Create a list of async tasks (one for each URL)
        tasks = [asyncio.create_task(check_url(session, url)) for url in URLS]
        
        # 2. Gather all tasks and run them concurrently
        results = await asyncio.gather(*tasks)

    # 3. Process and display metrics
    print("\n=== Project Metrics Summary ===")
    for res in results:
        if res["error"]:
            print(f"- {res['url']}: ERROR ({res['error']})")
        else:
            print(f"- {res['url']}: HTTP {res['status']} ({res['latency']:.2f}s)")
            
    total_time = time.time() - start_total
    print(f"\n⚡ Total execution time: {total_time:.2f} seconds")

if __name__ == "__main__":
    # The standard entry point to boot up the asyncio event loop
    asyncio.run(main())