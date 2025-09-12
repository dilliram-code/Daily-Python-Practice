**🔹1. What is Logging in Python?**

Logging is a way to record messages from your program while it runs.

`It helps in:`

- Debugging your code.
- Tracking events.
- Recording errors/warnings.
- Keeping history of program execution.
- Instead of using `print()`, Python’s `logging` module is more powerful, flexible, and professional.

**BASIC LOGGING EXAMPLE**
```python
import logging

# Basic configuration
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```
`Explanation:`

- `logging.debug()` → For debugging info (low-level details).

- `logging.info()` → General information.

- `logging.warning()` → Something unexpected but not breaking.

- `logging.error()` → A serious issue.

- `logging.critical()` → Very serious error.

`NOTE:`

⚡ Output will show only `WARNING`, `ERROR`, and `CRITICAL` by default unless you set `level=logging.DEBUG.`