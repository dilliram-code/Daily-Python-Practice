**🔹1. What is Logging in Python?**

Logging is a way to record messages from your program while it runs.

`It helps in:`

- Debugging your code.
- Tracking events.
- Recording errors/warnings.
- Keeping history of program execution.
- Instead of using `print()`, Python’s `logging` module is more powerful, flexible, and professional.

**🔹2. BASIC LOGGING EXAMPLE**
```pytho
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

**🔹 3. Logging Levels (in order of severity)**

- DEBUG → 10

- INFO → 20

- WARNING → 30

- ERROR → 40

- CRITICAL → 50

- The level you set decides which messages appear.
- `Example`: if you set `logging.basicConfig(level=logging.INFO)`, then `DEBUG` messages will not show.

**🔹 4. Formatting Log Messages**

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging details")
logging.info("Some useful information")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical issue")
```
