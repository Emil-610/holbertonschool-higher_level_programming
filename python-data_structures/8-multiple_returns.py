#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    return '{:c}'.format(sentence[0])
