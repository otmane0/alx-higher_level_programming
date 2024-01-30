#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
        tuple_b += (0,) * (2 - len(tuple_b))
        new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new
