#!/usr/bin/env python3

'''
find lines in a file that's not in another file
'''

import sys
import os

file = sys.argv[1]
file2 = sys.argv[2]

lines = open(file,'r').read().split('\n')
lines2 = open(file2,'r').read().split('\n')

print(f"in {file} but not {file2}:",file=sys.stderr)

for l in (set(lines) - set(lines2)):
	print(l)

