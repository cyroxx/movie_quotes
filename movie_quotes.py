#!/usr/bin/env python3

import random

with open('movie_quotes.txt', 'r') as f:
    lines = f.readlines()

l = random.choice(lines)
fields = l.split(' \t')

print('%s\n%s' % (fields[1], ('-- %s ' % fields[2]).rjust(64)))
