#!/usr/bin/python3
def uppercase(str):
    new = ''
    for i in str:
        if 97 <= ord(i) and ord(i) <= 122:
            new += chr(ord(i) - 32)
        else:
            new += i
    print(new)
