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
            things = files if item_type == 'file' else folders
        except PermissionError:
            print(f"Permission denied: {current_folder}")
            continue
        except Exception as e:
            print(f"Error reading {current_folder}: {e}")
            continue

        for thing in things:
            name_check = os.path.splitext(thing)[0] if item_type == 'file' else thing
            name_check_upper = name_check.upper()

            if match_type == 'exact' and name_check_upper == target_name_upper:
                found_items.append(os.path.join(current_folder, thing))
            elif match_type == 'contain' and target_name_upper in name_check_upper:
                found_items.append(os.path.join(current_folder, thing))
    return found_items

def start_search():
    print_ascii_art()
    path, item_type, name, match_type = get_user_input()

    if item_type not in ['file', 'directory']:
        print("Please enter 'file' or 'directory'.")
        return

    if match_type not in ['exact', 'contain']:
        print("Please enter 'exact' or 'contain'.")
        return

    if not os.path.exists(path):
        print("That path doesn't exist.")
        return

    if not os.path.isdir(path):
        print("That's not a directory.")
        return

    try:
        os.listdir(path)
    except PermissionError:
        print("You don't have permission to access this directory.")
        return
    except Exception as e:
        print(f"Can't read the directory: {e}")
        return

    results = search_items(path, item_type, name, match_type)

    if results:
        print("Found the following matches:")
        for result in results:
            print(result)
    else:
        print("No matches found.")

start_search()
