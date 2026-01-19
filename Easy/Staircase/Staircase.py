#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    counting_num = 1
    for num in range(n,0,-1):
        concat_string = ""
        for _ in range(num-1):
            concat_string += " "
        for _ in range(counting_num):
            concat_string+= "#" 
        counting_num += 1
        print(concat_string)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)