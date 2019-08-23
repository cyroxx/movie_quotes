#!/usr/bin/env python3

import random

with open('movie_quotes.txt', 'r') as f:
    lines = f.readlines()

l = random.choice(lines)
fields = l.split(' \t')

print(fields[1])
print(('-- %s ' % fields[2]).rjust(65), end='')
