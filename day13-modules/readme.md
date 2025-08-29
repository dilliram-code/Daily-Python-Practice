`Q1. Difference between math.pow and ** operator?`

- math.pow always returns float, while ** may return int.

`Q2. Difference between %, fmod, and remainder?`

- %: normal modulus
- fmod: float-friendly
- remainder: quotient is rounded to nearest integer

`Q3. Why use log1p(x) instead of log(1+x)?`

- For very small x, log1p(x) avoids floating-point precision errors.

`Q4. Difference between sqrt and isqrt?`

- sqrt: returns float
- isqrt: returns integer without floating error

**Interview Preparation Q&A for random module**

`Q1. Difference between random and secrets?`

- random → pseudo-random, deterministic, fast, not secure.
- secrets → cryptographically secure randomness, for passwords/tokens.

`Q2. Difference between random.randint() and random.randrange()?`

- randint(a, b) inclusive of both ends.
- randrange(a, b) → exclusive of b, works like range().

`Q3. How to make random numbers reproducible?`

- Use random.seed(value) to fix randomness.

`Q4. Which distribution to use in modeling heights of people?`

- Normal distribution (random.normalvariate).

`Q5. How to shuffle a list in place?`

- Use random.shuffle(list_name).

**🎯 Interview Preparation Q&A for `OS Module`**

***Q1. Difference between os.remove() and os.rmdir()?***

`👉 os.remove() deletes a file, while os.rmdir() removes an empty directory.`

***Q2. How do you list all files recursively?***

`👉 Use os.walk().`

***Q3. Why use os.path.join() instead of string concatenation?***

`👉 It automatically handles OS-specific separators (/ vs \).`

***Q4. How do you set and read environment variables in Python?***

`👉 os.environ["VAR"] = "value" and os.environ.get("VAR").`

***Q5. What’s the difference between os.system() and subprocess.run()?***

`👉 os.system() runs commands directly, subprocess.run() is safer and gives more control over input/output.`