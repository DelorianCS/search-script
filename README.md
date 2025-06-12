# Search Files Python Script (Linux Only)

A simple Python script to search for files or directories by name in a specified folder on Linux.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/search-files-script.git
cd search-files-script

    Make sure Python 3 is installed:

python3 --version

If not installed, install it with your package manager, for example on Ubuntu:

sudo apt update
sudo apt install python3

    (Optional) Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

    Make sure the script file search.py is in the repo folder.

Usage

Run the script in your terminal:

python3 search.py

You will be asked to provide some information step-by-step:

    Where do you want to search?
    Enter the full path of the folder where you want to start searching. For example: /home/yourusername/Documents

    Are you looking for a file or a directory? (file/directory)
    Type file if you want to search for files or directory if you want to search for folders.

    What name are you looking for?
    Enter the name or part of the name of the file or directory you want to find. For example: report or notes.

    Should the name match exactly or just contain it? (exact/contain)
    Type exact to find items with the exact name you typed, or contain to find any item whose name contains the text you provided.

After you answer these questions, the script will list all matching files or directories found, or notify you if there are no matches.
How It Works

    The script scans through all files and directories starting from the path you provided.

    It filters by your choice of files or directories.

    It checks the names for an exact or partial match depending on your input.

    All matching paths are displayed.

Do I Need to Upload the Script as a .py File?

Yes! Upload your Python script as a .py file (e.g., search.py) to your GitHub repository so others can download and use it easily.

Feel free to open issues or submit pull requests to improve the project!
