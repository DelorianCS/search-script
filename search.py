#!/usr/bin/env python3

import os

def get_user_input():
    search_path = input("Where do you want to search?: ").strip()
    item_type = input("Are you looking for a file or a directory? (file/directory): ").strip().lower()
    name_to_find = input("What name are you looking for?: ").strip()
    match_type = input("Should the name match exactly or just contain it? (exact/contain): ").strip().lower()
    return search_path, item_type, name_to_find, match_type

def search_items(path, item_type, target_name, match_type):
    found_items = []
    for current_folder, folders, files in os.walk(path):
        if item_type == 'file':
            items_to_check = files
        else:
            items_to_check = folders
        
        for item in items_to_check:
            name_for_comparison = os.path.splitext(item)[0] if item_type == 'file' else item
            
            if match_type == 'exact' and name_for_comparison == target_name:
                found_items.append(os.path.join(current_folder, item))
            elif match_type == 'contain' and target_name in name_for_comparison:
                found_items.append(os.path.join(current_folder, item))
    return found_items

def main():
    path, item_type, name, match_type = get_user_input()

    if item_type not in ['file', 'directory']:
        print("Please enter 'file' or 'directory'.")
        return

    if match_type not in ['exact', 'contain']:
        print("Please enter 'exact' or 'contain'.")
        return

    if not os.path.isdir(path):
        print("The path doesn't exist or is not a directory.")
        return

    results = search_items(path, item_type, name, match_type)

    if results:
        print("Found the following matches:")
        for result in results:
            print(result)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
