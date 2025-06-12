<h1 align="center">🔍 File/Directory Search Script</h1>

![Preview](Peek-View.gif)

## Features

- 🔍 Search for files or directories by name  
- 🎯 Choose between exact matches or partial containment  
- 🔄 Recursive search through all subdirectories  
- 💻 Simple interactive command-line interface  
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
nano ~/.bashrc  | or ~/.zshrc
```

Add this at the bottom:
```bash
search() { python3 /FULL/PATH/TO/search.py ; }
```

Now you can run `search` in any terminal window!

---

## 🚀 Usage (Interactive Mode)

The script will ask you a few questions:

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
> Just the name, **without extension**.  
> ❌ `file.txt` → ❌  
> ✅ `file` → ✅

```
Should the name match exactly or just contain it? (exact/contain):
```

After that, the search begins — and you'll see matching results printed out.

---

## ❤️ Thanks for reading

Hope you found this script useful!  
Suggestions and contributions are welcome.
