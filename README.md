<h1 align="center">🔍 File/Directory Search Script</h1>

![Preview](Peek-View.gif)

## Features

- 🔍 Search for files or directories by name  
- 🎯 Choose between exact matches or partial containment  
- 🔄 Recursive search through all subdirectories  
- 💻 Interactive *or* command-line interface  
- ⚡ Fast scanning using native Python `os.walk()`

---

## 🛠 Installation

1. Make sure you are on Linux  
2. Confirm that Python 3 is installed  
3. Clone the repository:

```bash
git clone https://github.com/DelorianCS/search-script.git
cd search-script
python3 search.py
```

✅ You can also make it a terminal command:

```bash
nano ~/.bashrc  # or ~/.zshrc
```

Add this at the bottom:
```bash
search() { python3 /FULL/PATH/TO/search.py "$@" ; }
```

Now you can use `search` as a custom command.

---

## Usage Options

### 🧑 Interactive Mode (default)
If no arguments are provided, the script will prompt you step by step:

```
Where do you want to search?:
```
> Example: `/home/user/Downloads/`

```
Are you looking for a file or a directory? (file/directory):
```

```
What name are you looking for?:
```
> Just the name, without extension.  
> ❌ `file.txt` → ❌  
> ✅ `file` → ✅

```
Should the name match exactly or just contain it? (exact/contain):
```

---

### ⚙️ Command-Line Mode

Use the script with flags to skip prompts:

```bash
python3 search.py -p /home/user/docs -k file -n report -m contain
```

#### 🔧 Available arguments:

| Flag            | Description                             |
|-----------------|-----------------------------------------|
| `-p` `--path`   | Path to start the search                |
| `-k` `--kind`   | `file` or `directory`                   |
| `-n` `--name`   | Name to search (without extension)      |
| `-m` `--match`  | `exact` or `contain`                    |

---

## ❤️ Thanks for reading

Hope you found this script useful!  
Suggestions and contributions are welcome.
