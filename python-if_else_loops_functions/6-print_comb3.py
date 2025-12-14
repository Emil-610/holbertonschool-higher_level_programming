#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print('{:02d},'.format(i), end=' ')
    elif i < 89:
        a = i // 10
        b = i % 10
        j = b * 10 + a
        if j > i and a != b:
            print('{},'.format(i), end=' ')
    else:
        a = i // 10
        b = i % 10
        j = b * 10 + a
        if j > i and a != b:
            print('{}'.format(i))
