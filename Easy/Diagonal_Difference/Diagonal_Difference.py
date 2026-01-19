#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    reversed_arr= list(reversed(arr))
    left_to_right_sum = 0
    right_to_left_sum = 0
    for index in range(len(arr)):
       left_to_right_sum += arr[index][index] 
       right_to_left_sum += reversed_arr[index][index]
    return abs(left_to_right_sum - right_to_left_sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()