#!/usr/bin/env python3

# URL encode input form stidin

import sys
import binascii

s=input()
while True:

	
	bs=binascii.hexlify(s.encode()).decode()
	for i in range(0,len(bs)):
		if i % 2 == 0:
			print("%",end='')
		print(bs[i],end='')
	print()
	try:
		s = input()
	except:
		exit(0)
	if len(s) < 1:
		break
