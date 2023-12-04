#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}

    x = (a.union(b)).intersection(d)
    y = (set()).intersection(d).union(c.difference(b))

    if not x:
        print("x - пустое множество")
    else:
        print(f'x = {x}')

    if not y:
        print("y - пустое множество")
    else:
        print(f'y = {y}')
