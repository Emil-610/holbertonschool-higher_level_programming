#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_val = None

    for k, v in a_dictionary.items():
        if best_val is None or v > best_val:
            best_val = v
            best_key = k

    return best_key
