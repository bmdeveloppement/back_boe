# -*- coding: utf-8 -*-

def copy_items(from_obj, to_obj, items):
    for item in items:
        setattr(to_obj, item, from_obj[item])