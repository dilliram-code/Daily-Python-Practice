**1. What is JSON?**

- JSON stands for `JavaScript Object Notation.`
- It’s a lightweight data format for storing and exchanging data.
- Widely used in APIs, configuration files, databases.

`👉 JSON looks like a Python dictionary, but it is actually a string.`

Example JSON:
```python
{
  "name": "Alice",
  "age": 25,
  "is_student": false,
  "skills": ["Python", "Machine Learning", "Data Science"],
  "address": { "city": "Kathmandu", "country": "Nepal" }
}
```
**2. JSON in Python**
- Python has a built-in module called json.
```python
import json
```
This module provides:

- `json.dumps()` → Convert Python → JSON string
- `json.loads()` → Convert JSON string → Python object
- `json.dump()` → Write JSON to a file
- `json.load()` → Read JSON from a file