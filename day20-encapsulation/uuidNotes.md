**What is a UUID?**

- `UUID`: A 128-bit number used to uniquely identify information.

- Represented as a 32-character hexadecimal string, divided by hyphens into 5 groups:
```python
550e8400-e29b-41d4-a716-446655440000
```
- Ensures uniqueness across time and space.

**Types of UUIDs in Python**

Python’s uuid module supports 5 variants:

- `UUID1` – based on time & MAC address

- `UUID3` – based on MD5 hashing (name-based)

- `UUID4` – random UUID

- `UUID5` – based on SHA-1 hashing (name-based)

- `UUID objects` – represents UUIDs with methods.

`Best Practices:`

- ✅ Use `uuid4()` for random unique IDs (most common).
- ✅ Use `uuid1()` when you want time-based ordering (but it leaks MAC/time info).
- ✅ Use `uuid3()` or `uuid5()` for consistent deterministic IDs.
- ❌ Don’t use UUID as a replacement for cryptographic randomness — it’s unique, but not always secure.