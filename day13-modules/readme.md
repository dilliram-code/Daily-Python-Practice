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

