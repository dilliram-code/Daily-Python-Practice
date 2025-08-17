- A dictionary in Python is a `built-in` data type that stores data in key-value pairs.
- It is unordered (before Python 3.7), but since Python 3.7+, dictionaries maintain insertion order.

**Keys to Note down**
- ✅ Keys are unique and must be immutable types (string, number, tuple).
- ✅ Values can be of any type (list, int, dict, etc.).



## 📌 Dictionary vs List – When to Use?

### ✅ Use **Dictionary (`dict`)** when:
- You need **fast lookup** by a **unique key**.  
- Data is best represented as **key-value pairs**.  
- Example: Storing student IDs with their names.

### ✅ Use **List (`list`)** when:
- You care about **ordering** of items.  
- You don’t need **key-based access**.  
- Example: Maintaining a sequence of tasks.

## 📌 Dictionary Best Practices

- ✅ Use `.get()` to avoid **KeyError**.  
- ✅ Prefer **dictionary comprehension** for clean and readable code.  
- ✅ Use **immutable types** (`str`, `int`, `tuple`) as keys.  
- ✅ For missing keys, use **`defaultdict`** or **`setdefault()`**.  
- ✅ When merging, prefer `{**dict1, **dict2}` for clarity.

## ⚡ Weird or Tricky Things About Python Dictionaries

### 1. Keys must be **hashable (immutable)**
- Keys in dictionaries must be **hashable**, meaning their value should not change during their lifetime.  
- ✅ Allowed: `str`, `int`, `tuple` (if it contains only hashable elements).  
- ❌ Not allowed: `list`, `dict` (since they are mutable).  

```python
# ✅ Valid keys
my_dict = {
    "name": "Alice",
    42: "Answer",
    (1, 2): "Tuple as key"
}

# ❌ Invalid key (raises TypeError)
my_dict = {
    [1, 2, 3]: "List as key"   # ❌ Not hashable
}
```
### 2. Dictionary keys are **unique — last assignment wins**
- If you repeat a key, the dictionary will **overwrite the earlier value**.  

```python
d = {"a": 1, "b": 2, "a": 3}
print(d)  
# Output: {'a': 3, 'b': 2}
```

### 3. Iteration order is **insertion order** (since Python 3.7)
- Dictionaries preserve the order of insertion of keys.  

```python
d = {"x": 1, "y": 2, "z": 3}
print(list(d.keys()))   
# Output: ['x', 'y', 'z']
```
- ⚠️ In older Python versions (<3.7), the order was not guaranteed.

### 4. Shallow copies vs Deep copies
- Using `.copy()` or `dict()` makes a **shallow copy** → nested objects are **shared**.  
- Use `copy.deepcopy()` for **independent copies**.  

```python
import copy

d1 = {"a": [1, 2]}
d2 = d1.copy()
d2["a"].append(3)

print(d1)  
# Output: {'a': [1, 2, 3]}  <-- changed both
```
### 5. Merging dictionaries
- Python **3.9+** introduced the **merge (`|`)** and **update (`|=`)** operators.
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print(d1 | d2)   
# Output: {'a': 1, 'b': 3, 'c': 4}

d1 |= d2
print(d1)        
# Output: {'a': 1, 'b': 3, 'c': 4}
```

### 6. Default dictionary behavior (`get` vs `[]`)
- Accessing a **missing key** with `[]` raises **KeyError**.  
- Using `.get()` returns **None** (or a default value you provide).  

```python
d = {"x": 10}

print(d.get("y"))      # Output: None
print(d.get("y", 0))   # Output: 0

# print(d["y"])        # ❌ KeyError