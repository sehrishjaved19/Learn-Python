# 📂 07_File_IO
Welcome to the **File Input and Output (File I/O)** section!  
In this section, you’ll learn how Python interacts with files — reading data, writing new content, appending text, and using the `with` statement for efficient and safe file handling.

File handling is essential for real projects because it lets your programs **store**, **retrieve**, and **process** data persistently.

---

## 📘 Overview

Here you’ll explore:
- How to **open and close** files properly.  
- File **modes**: read (`r`), write (`w`), append (`a`) (and notes about `x`, `t`, `b`).  
- Reading data using `read()`, `readline()`, and `readlines()`.  
- Writing (overwrite) and appending (add) operations.  
- Using the **`with` statement** (context manager) to automatically close files.  

---
# 📂 07_File_IO

```

07_File_IO/
│
├── 01_file_basics.py
├── 02_read_file.py
├── 03_write_file.py
├── 04_append_file.py
├── 06_with_statement.py
├── file.txt
├── poem.txt
├── Practice_Exercises/
└── README.md

```

---

## 🧩 Files Description

| File Name | Description |
|---|---|
| `01_file_basics.py` | Intro to file handling: `open()`, `close()`, basic `read()` example and explanation of file modes. |
| `02_read_file.py` | Demonstrates `read()`, `readline()` and `readlines()`. Shows reading with loops and `.strip()` to clean newline characters. |
| `03_write_file.py` | Shows how to write to a file with mode `"w"` (overwrites existing content). |
| `04_append_file.py` | Demonstrates appending text to an existing file using mode `"a"` (preserves existing content). |
| `06_with_statement.py` | Explains and demonstrates `with open(...) as f:` — best practice for auto-closing files and safe handling. |
| `file.txt`, `poem.txt` | Example data files used by the above scripts. |
| `Practice_Exercises/` | Folder for hands-on tasks (word counter, merge files, file cleaner, etc.). |

---

## 🧠 Example Code Snippets

### Read whole file (basic)
```python
# 01_file_basics.py (snippet)
f = open('file.txt', 'r')
content = f.read()
print(content)
f.close()
```

### Read line-by-line and readlines()

```python
# 02_read_file.py (snippet)
with open('file.txt', 'r') as f:
    lines = f.readlines()   # returns a list of lines
    for line in lines:
        print(line.strip())
```

### Write (overwrite) a file

```python
# 03_write_file.py (snippet)
st = 'A thing of beauty is a joy forever!'
with open('myfile.txt', 'w') as f:
    f.write(st)
```

### Append to a file

```python
# 04_append_file.py (snippet)
st = "\n(Author: John Keats)"
with open('myfile.txt', 'a') as f:
    f.write(st)
```

### Using `with` (context manager)

```python
# 06_with_statement.py (snippet)
with open('file.txt', 'r') as f:
    print(f.read())
# file auto-closed here
```

---

## 🎯 Learning Goals

By the end of this section you should be able to:

* Explain and use the main file modes (`r`, `w`, `a`) and know when to use each.
* Read files fully or line-by-line and process the content.
* Write and append text files safely.
* Use `with open()` to manage files without explicit `close()` calls.
* Implement small file-based utilities (counters, mergers, cleaners).



## ✅ Tips & Best Practices

* Prefer `with open(...)` for file operations — it’s safer and cleaner.
* Use `.strip()` when printing lines to avoid extra blank lines.
* Never hard-code absolute file paths if you plan to share the repo — use relative paths.
* Avoid storing secrets or credentials in plain text files in the repo.
* Add `Practice_Exercises/README.md` documenting each practice file briefly.

---

**Next Section →** [08_Exceptions_Debugging](../08_Exceptions_Debugging/README.md)

---
