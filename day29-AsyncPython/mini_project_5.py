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