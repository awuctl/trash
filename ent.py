#!/usr/bin/env python

import argparse
from math import sqrt, log2
from functools import reduce
import statistics

def get_frequency(data: bytes) -> list:

    size = len(data)
    freq = [0]*256

    for byte in data:
        freq[int(byte)] += 1
    
    for i in range(len(freq)):
        freq[i] = freq[i] / size
    
    return freq

def calc_entropy(data: bytes) -> float:
    size = len(data)
    freq = get_frequency(data)
    
    return -reduce(lambda a, x: a + x*log2(x) if x != 0 else a, freq, 0.0)

if __name__ == '__main__':
    
    p = argparse.ArgumentParser(description='Calculate Shannon entropy of a file.')
    p.add_argument('files', type=argparse.FileType(mode='rb'), nargs='*', help='File(s) to parse')
    p.add_argument('-n', help='Print filenames', default=False, action='store_true')
    args = p.parse_args()

    if args.n:
        for file in args.files:
            print(file.name, calc_entropy(file.read()), sep='\t')
    else:
        for file in args.files:
            print(calc_entropy(file.read()))
