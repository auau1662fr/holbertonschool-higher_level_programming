#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Step 1: Load existing list
try:
    items = load_from_json_file(filename)
except Exception:
    items = []

# Step 2: Add new arguments
for arg in sys.argv[1:]:
    items.append(arg)

# Step 3: Save back to file
save_to_json_file(items, filename)
