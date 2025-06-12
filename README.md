
# File/Directory Search Script

A Python script to recursively search for files or directories by name with exact or partial matching.

## Features

### 🔍 Search for files or directories by name
### ⚙️ Choose between exact matches or partial containment
### 📂 Recursive search through all subdirectories
### 💻 Simple interactive command-line interface
### 🚀 Fast scanning using native Python `os.walk()`

## Installation
1. Make sure you are on Linux
1. Confirm that Python 3 is installed
2. Clone the repository:

```
git clone https://github.com/DelorianCS/search-script.git
cd search-script
python search.py
```
You can also add it as a command like this
```
nano ~/.bashrc / ~/.zshrc
```
And add this at the very end
```
search() {python3 /directory/search.py}
```
#### And now you can do `search` on your terminal and use the script from there!

## Usage
  Basic Usage
```
  Where do you want to search?:
```
  Select a directory (e.g. "/home/user/Downloads/"
```
  Are you looking for a file or a directory?
```
  Select which one you want to search for (file/directory)
  ```
  What name are you looking for?
```
  Select what name you want to search for (e.g. flag)
```
  Should the name match exactly or just contain it?
```
  Pick one (exact/contain) 
  #### CAREFUL, do not type the file extension
  
## Requirements

  - Python3
  - Any Linux distro
