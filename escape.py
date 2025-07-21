a='\'sehrish\' is learning python!\n and expanding her knowledge\t (this is my sample of hand\'s-on practice of using escape sequences in python)'
print(a)


# | Escape Sequence | Description                           | Example Output                       |
# | --------------- | ------------------------------------- | ------------------------------------ |
# | `\'`            | Single quote                          | `'I\'m happy' → I'm happy`           |
# | `\"`            | Double quote                          | `"He said: \"Hi!\""`                 |
# | `\\`            | Backslash                             | `"C:\\new\\folder"`                  |
# | `\n`            | New line                              | `"Hello\nWorld"`                     |
# | `\t`            | Horizontal tab                        | `"Name:\tSehrish"`                   |
# | `\r`            | Carriage return (moves to line start) | `"12345\rABC"` → `ABC45`             |
# | `\b`            | Backspace                             | `"abc\b"` → `ab`                     |
# | `\f`            | Form feed                             | (rarely used)                        |
# | `\v`            | Vertical tab                          | (rarely used)                        |
# | `\ooo`          | Character with octal value `ooo`      | `\101` → `'A'`                       |
# | `\xhh`          | Character with hex value `hh`         | `\x41` → `'A'`                       |
# | `\uXXXX`        | Unicode character (4 hex digits)      | `\u03A9` → `'Ω'`                     |
# | `\UXXXXXXXX`    | Unicode character (8 hex digits)      | `\U0001F600` → 😀                    |
# | `\N{name}`      | Unicode character by name             | `\N{GREEK CAPITAL LETTER DELTA}` → Δ |
