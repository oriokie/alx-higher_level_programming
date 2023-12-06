#!/usr/bin/python3
"""
7. Load, add, save

"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
save_to_json_file(my_list + sys.argv[1:], "add_item.json")
