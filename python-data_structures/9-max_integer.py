#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    res = -1
    for i in my_list:
        if res < i:
            res = i
    return res
