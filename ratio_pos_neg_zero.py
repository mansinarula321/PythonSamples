#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_count = 0.0
    neg_count = 0.0
    zero_count = 0.0
    ratio_pos = 0.0
    ratio_neg = 0.0
    ratio_zero = 0.0
    for x in arr:
        if x > 0:
            pos_count = pos_count + 1.0
        if x < 0:
            neg_count = neg_count + 1.0
        if x == 0:
            zero_count = zero_count + 1.0

    ratio_pos = round(pos_count / len(arr), 6)
    ratio_neg = round(neg_count / len(arr), 6)
    ratio_zero = round(zero_count / len(arr), 6)
    print('%0.6f' % ratio_pos)
    print('%0.6f' % ratio_neg)
    print('%0.6f' % ratio_zero)


if __name__ == '__main__':
    #!n = int(input().strip())

    #!arr = list(map(int, input().rstrip().split()))
    arr=[1,1,0,-1,-1]


    plusMinus(arr)
