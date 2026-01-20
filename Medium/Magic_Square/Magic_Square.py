#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

from itertools import permutations

def is_magic(p):
    return (
        p[0] + p[1] + p[2] == 15 and
        p[3] + p[4] + p[5] == 15 and
        p[6] + p[7] + p[8] == 15 and
        p[0] + p[3] + p[6] == 15 and
        p[1] + p[4] + p[7] == 15 and
        p[2] + p[5] + p[8] == 15 and
        p[0] + p[4] + p[8] == 15 and
        p[2] + p[4] + p[6] == 15
    )

def formingMagicSquare(square):
    flat = [square[i][j] for i in range(3) for j in range(3)]
    min_cost = float('inf')

    for p in permutations(range(1, 10)):
        if is_magic(p):
            cost = sum(abs(flat[i] - p[i]) for i in range(9))
            min_cost = min(min_cost, cost)

    return min_cost
