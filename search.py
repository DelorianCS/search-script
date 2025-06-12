#!/usr/bin/env python3
import os

def print_ascii_art():
    art = r"""
  _____                     _        _____           _       _   
 / ____|                   | |      / ____|         (_)     | |  
| (___   ___  __ _ _ __ ___| |__   | (___   ___ _ __ _ _ __ | |_ 
 \___ \ / _ \/ _` | '__/ __| '_ \   \___ \ / __| '__| | '_ \| __|
 ____) |  __/ (_| | | | (__| | | |  ____) | (__| |  | | |_) | |_ 
|_____/ \___|\__,_|_|  \___|_| |_| |_____/ \___|_|  |_| .__/ \__|
                                                      | |        
                                                      |_|       
"""
    print(art)

def get_user_input():
    search_path = input("Where do you want to search?: ").strip()
    item_type = input("Are you looking for a file or a directory? (file/directory): ").strip().lower()
    name_to_find = input("What name are you looking for?: ").strip()
    match_type = input("Should the name match exactly or just contain it? (exact/contain): ").strip().lower()
    return search_path, item_type, name_to_find, match_type

def search_items(path, item_type, target_name, match_type):
    found_items = []
    target_name_upper = target_name.upper()
    for current_folder, folders, files in os.walk(path, onerror=lambda e: None):
        try:
            # Decide whether to look for files or directories
            candidates = files if item_type == 'file' else folders
        except PermissionError:
            print(f"Permission denied for: {current_folder}. Skipping...")
            continue
        except Exception as e:
            print(f"Error accessing {current_folder}: {e}. Skipping...")
            continue

        for candidate in candidates:
            # Strip extension for files, keep directory names as is
            name_check = os.path.splitext(candidate)[0] if item_type == 'file' else candidate
            name_check_upper = name_check.upper()

            if match_type == 'exact' and name_check_upper == target_name_upper:
                found_items.append(os.path.join(current_folder, candidate))
            elif match_type == 'contain' and target_name_upper in name_check_upper:
                found_items.append(os.path.join(current_folder, candidate))
    return found_items

def start_search():
    print_ascii_art()
    path, item_type, name, match_type = get_user_input()

    if item_type not in ('file', 'directory'):
        print("Oops! Please enter either 'file' or 'directory'.")
        return

    if match_type not in ('exact', 'contain'):
        print("Please type 'exact' or 'contain' to specify the match type.")
        return

    if not os.path.exists(path):
        print(f"Sorry, the path '{path}' doesn't exist.")
        return

    if not os.path.isdir(path):
        print(f"Looks like '{path}' is not a directory.")
        return

    try:
        os.listdir(path)
    except PermissionError:
        print("You don't have permission to access this directory. Try another path.")
        return
    except Exception as e:
        print(f"Unexpected error reading the directory: {e}")
        return

    results = search_items(path, item_type, name, match_type)

    if results:
        print("\nMatches found:")
        for item in results:
            print(item)
    else:
        print("\nNo matches found. Maybe try a different name or path?")

if __name__ == "__main__":
    start_search()
