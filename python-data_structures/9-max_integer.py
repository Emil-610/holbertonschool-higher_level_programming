#!/usr/bin/python3
def max_integer(my_list=[]):
    res = -1
    for i in my_list:
        if res < i:
            res = i
    return res
