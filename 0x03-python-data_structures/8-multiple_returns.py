#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        lenn = 0
        f_char = None
        return (lenn, None)

    lenn = len(sentence)
    for i in sentence:
            f_char = i
            break

    return (lenn, f_char)