**Interview questions `(with brief answers)`**
***Basic***

Q: `How are strings stored in Python 3?`
- As Unicode code points in str objects; bytes are sequences of raw bytes.

Q: `How do you reverse a string?`
- `s[::-1]` or `''.join(reversed(s))`.

Q: `Why is ''.join(list_of_strings) preferred over repeated +=?`
- join is O(n), repeated concatenation in a loop is O(n²) due to creating many intermediate strings.

Q: `How to check if string s contains only digits?`
- `s.isdigit()` (note locale/Unicode nuances), or `s.isnumeric()` depending on needs.