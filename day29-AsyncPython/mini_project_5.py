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