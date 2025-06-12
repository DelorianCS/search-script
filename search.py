#!/usr/bin/env python3
import os

print(r"""
  _____                     _        _____           _       _   
 / ____|                   | |      / ____|         (_)     | |  
| (___   ___  __ _ _ __ ___| |__   | (___   ___ _ __ _ _ __ | |_ 
 \___ \ / _ \/ _` | '__/ __| '_ \   \___ \ / __| '__| | '_ \| __|
 ____) |  __/ (_| | | | (__| | | |  ____) | (__| |  | | |_) | |_ 
|_____/ \___|\__,_|_|  \___|_| |_| |_____/ \___|_|  |_| .__/ \__|
                                                      | |        
                                                      |_|       
""")

path = input("Where do you want to search?: ").strip()
kind = input("Are you looking for a file or a directory? (file/directory): ").strip().lower()
name = input("What name are you looking for?: ").strip()
match = input("Should the name match exactly or just contain it? (exact/contain): ").strip().lower()

if kind not in ("file", "directory"):
    print("Oops! Please enter either 'file' or 'directory'.")
    exit(1)
elif match not in ("exact", "contain"):
    print("Please type 'exact' or 'contain' to specify the match type.")
    exit(1)
elif not os.path.isdir(path):
    print(f"Sorry, the path '{path}' doesn't exist or is not a directory.")
    exit(1)

try:
    os.listdir(path)
except Exception as e:
    print(f"Can't access path: {e}")
    exit(1)

results = []

target = name.lower()

for root, dirs, files in os.walk(path):
    items = files if kind == "file" else dirs
    for item in items:
        check = os.path.splitext(item)[0] if kind == "file" else item
        check = check.lower()

        if match == "exact":
            if check == target:
                results.append(os.path.join(root, item))
        elif target in check:
            results.append(os.path.join(root, item))

if results:
    print("\nMatches found:")
    for r in results:
        print(r)
else:
    print("\nNo matches found. Maybe try a different name or path?")
