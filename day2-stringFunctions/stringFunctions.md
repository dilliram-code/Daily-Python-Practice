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

**Intermediate**

Q: `Difference between str.find() and str.index()?`
-  `find()` returns `-1` if not found; `index()` raises `ValueError`.

Q: `Explain str.format() vs f-strings.`
- f-strings are evaluated at runtime and can include expressions; `format()` is older, useful when template is dynamic.

Q: `How to handle Unicode normalization?`
- Use unicodedata.normalize('NFC'|'NFD'|'NFKC'|'NFKD', s) before comparisons.

Q: `How to perform safe templating for user content?`
- Use string.Template or sanitized templates; do not evaluate user input with eval/format that may include code.

**Advanced**

Q: `What is a grapheme cluster and why does it matter?`
- A user-perceived character may be multiple code points (base+combining marks). Operations like slicing by code points can split graphemes; use grapheme-aware libraries when needed.

Q: `How to efficiently search many patterns in text?`
- Compile regexes, use re.compile() once; for many fixed substrings consider Aho-Corasick algorithm (third-party libs).

Q: `How do you prevent DoS via giant format strings or crafted input?`
- Validate template size and placeholders; avoid formatting untrusted user templates with powerful features; use Template or whitelist format fields.

Q: `Explain Python’s string interning.`
- Small immutable strings may be interned to reuse memory and speed up comparisons; sys.intern() explicitly interns strings.

Q: `How to handle text encoding issues when reading files from unknown sources?`
- Try utf-8 with errors='replace' or detect encoding with chardet/charset-normalizer; normalize text afterward.