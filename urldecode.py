#!/usr/bin/env python3

'''
decodes strings from args or stdin
'''

from argparse import ArgumentParser
from sys import stdin, stdout
from urllib.parse import unquote_plus as url_decode

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("string", nargs="*")
    args = parser.parse_args()

    if args.string:
        print(url_decode(" ".join(args.string)), end='\n')
    else:
        print(url_decode(stdin.read()[:-1]), end='\n')
