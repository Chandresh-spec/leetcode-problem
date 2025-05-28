#string?
#strings is sequence of character enclosed in single or double quotes

example="hello"

# Immutable: Strings cannot be changed after creation.

# Indexing: Access characters using index.

s = "hello"
print(s[0])     # 'h'
print(s[-1])    # 'o'


# Slicing:
print(s[1:4])     # 'ell'
print(s[::-1])



# | Method                 | Description                             |
# | ---------------------- | --------------------------------------- |
# | `s.lower()`            | Convert to lowercase                    |
# | `s.upper()`            | Convert to uppercase                    |
# | `s.strip()`            | Remove leading/trailing whitespace      |
# | `s.replace(old, new)`  | Replace substring                       |
# | `s.find(sub)`          | Find first occurrence (-1 if not found) |
# | `s.startswith(prefix)` | Check if starts with                    |
# | `s.endswith(suffix)`   | Check if ends with                      |
# | `s.split(delim)`       | Split into list                         |
# | `s.join(list)`         | Join list with string                   |
# | `s.count(sub)`         | Count occurrences of substring          |
