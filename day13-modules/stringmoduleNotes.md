**Introduction to string Module**

`Python’s string module provides:`

- Constants (like all alphabets, digits, punctuation)
- Useful string functions (helper functions for text processing)
```python
import string
```
**Constants in string**

`string.ascii_letters`
- All lowercase + uppercase English alphabets.
```python
import string
print(string.ascii_letters)  

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```
`string.ascii_lowercase`
```python
print(string.ascii_lowercase)  

# abcdefghijklmnopqrstuvwxyz
```
`string.ascii_uppercase`
```python
print(string.ascii_uppercase) 

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
`string.digits`
```python
print(string.digits)  

# 0123456789
```
`string.hexdigits`
```python
print(string.hexdigits)  

# 0123456789abcdefABCDEF
```
`string.octdigits`
```python
print(string.octdigits)  

# 01234567
```
`string.punctuation`
```python
print(string.punctuation)  

# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

`string.printable`
```python
print(string.printable)

# All printable characters: digits, letters, punctuation, whitespace.
```
`string.whitespace`
```python
print(repr(string.whitespace))  

# ' \t\n\r\x0b\x0c'
```