#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    arrysum = 0
    for i in range(len(arr)):
        if i == 0:
            min = arr[i]
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]

    for i in range(len(arr)):
        arrysum = arrysum + arr[i]

    minSum = arrysum - max
    maxSum = arrysum - min
    print(str(minSum) + ' ' + str(maxSum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
