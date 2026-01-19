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
    total_nums = len(arr)
    positive= 0
    negative=0
    zero=0
    for num in arr:
        match num:
            case num if num > 0:
                positive += 1
            case num if num < 0:
                negative += 1
            case 0:
                zero += 1
    print(format(positive/total_nums,".6f"))
    print(format(negative/total_nums,".6f"))
    print(format(zero/total_nums,".6f"))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)