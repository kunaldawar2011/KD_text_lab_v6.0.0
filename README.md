# KD Text Lab v6.0.0

A simple terminal-based text editor written in Python. You write text, and it is saved to a file. You can then run 13 text operations on that file, such as counting words, changing case, reversing, splitting, and searching. Output is colored and includes short animation delays.

Developed by **Kunal Dawar** (GitHub: [@kunaldawar2011](https://github.com/kunaldawar2011))

---

## Description

KD Text Lab is a lightweight command-line tool that needs no GUI or IDE. It works on Linux, macOS, Windows, and Android (Termux).

When you start the program, it shows the platform you are running on and asks for your name. From the main menu, you can write new text, which is appended to a text file. The text menu then lets you run operations on the saved file. Some operations only print the result, and others also save the changed text back to the file.

---

## Additional Description

### Key Features

- Shows the operating system platform at startup (using `sys.platform`)
- Personalized greeting
- Appends each new entry to a text file
- 13 text operations: word count, character count, case conversion, reverse, split, title case, alphabet and digit checks, and search
- Shows how many seconds the session has been running
- Colored output with short animation delays

### How It Works

1. Run the script and enter your name.
2. In the main menu, choose `1` to edit text or `2` to exit.
3. Type your text. It is added to `filecreatedfromKD_text_lab_v6.0.0.txt`.
4. In the text menu, choose an operation by number.
5. Choose `14` to exit the program.

### Project Structure

```
KD_text_lab_v6.0.0/
├── KD_text_editor_6.0.0.py   # Main script
├── README.md                 # Project documentation
└── .gitignore                # Ignores the generated output file
```

The output file `filecreatedfromKD_text_lab_v6.0.0.txt` is created automatically in the folder where you run the script.

---

## Requirements

- Python **3.10 or above** (the script uses `match` statements)
- pip
- Git (only needed to clone the repository)

## Dependencies

| Module | Type | Purpose |
|---|---|---|
| `time` | Built-in | Animation delays and session timing |
| `random` | Built-in | Imported (not used in the current version) |
| `sys` | Built-in | Shows the current platform |
| `colorama` | External (pip) | Colored terminal output |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/kunaldawar2011/KD_text_lab_v6.0.0.git
cd KD_text_lab_v6.0.0

# Install colorama
pip install colorama

# Run the program
python KD_text_editor_6.0.0.py
```

On Linux and macOS, use `pip3` and `python3` if `pip` or `python` is not found.

**Termux:**

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/kunaldawar2011/KD_text_lab_v6.0.0.git
cd KD_text_lab_v6.0.0
python -m pip install colorama
python KD_text_editor_6.0.0.py
```

---

## Menu Reference

| No. | Operation | What it does | Changes the file? |
|---|---|---|---|
| 1 | Count words | Shows the number of words | No |
| 2 | Uppercase | Converts text to UPPERCASE | Yes |
| 3 | Lowercase | Converts text to lowercase | Yes |
| 4 | Reverse | Reverses the text | Yes |
| 5 | Count characters | Shows the total number of characters | No |
| 6 | Alphabet test | Checks if the text has only letters | No |
| 7 | Number test | Checks if the text has only digits | No |
| 8 | Split | Splits the text into a list of words | Yes |
| 9 | Swap case | Swaps uppercase and lowercase | Yes |
| 10 | Title case | Capitalizes the first letter of each word | Yes |
| 11 | Capitalize | Capitalizes the first letter of the text | Yes |
| 12 | Find | Finds a word or character and shows its index | No |
| 13 | Session time | Shows seconds since the program started | No |
| 14 | Exit | Closes the program | No |

> **Warning:** Operations marked "Yes" overwrite the output file. Keep a backup of important text.

---

## Known Issues

- **Option 2** uses the annotation `Unknown`, which is not defined. This can crash the program with a `NameError`. Fix: change `data: Unknown = ...` to `data = ...`.
- **Option 7** uses the variable `is_aplha`, which is not defined in that branch. This can cause a `NameError`. Fix: check `is_num == False` instead.
- **Option 5** is labeled "count alphabet (including space)" but returns the total character count.
- **Option 8** saves the split result in Python list format (for example, `['hello', 'world']`).

---

## Contributing

1. Fork the repository.
2. Create a branch: `git checkout -b fix/your-fix`
3. Commit your changes: `git commit -m "Describe your change"`
4. Push the branch: `git push origin fix/your-fix`
5. Open a Pull Request.

---

## Author

**Kunal Dawar**
GitHub: [@kunaldawar2011](https://github.com/kunaldawar2011)
