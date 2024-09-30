#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)

    lenn = len(sentence)
    f_char = sentence[0]

    return (lenn, f_char)