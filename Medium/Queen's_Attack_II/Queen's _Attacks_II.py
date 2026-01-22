#!/bin/python3

import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    right=[]
    left=[]
    up=[]
    down=[]
    diag_right_up=[]
    diag_right_down=[]
    diag_left_up=[]
    diag_left_down=[]
    total_attacks=0

    # we will sort out all the obstacles into direction
    # store obstacles as tuples
    for pawn in obstacles:
        # RIGHT
        if pawn[0] == r_q and pawn[1] > c_q:
            right.append((pawn[0], pawn[1]))
        # LEFT
        elif pawn[0] == r_q and pawn[1] < c_q:
            left.append((pawn[0], pawn[1]))
        # UP
        elif pawn[0] > r_q and pawn[1] == c_q:
            up.append((pawn[0], pawn[1]))
        # DOWN
        elif pawn[0] < r_q and pawn[1] == c_q:
            down.append((pawn[0], pawn[1]))
        # DIAGONALS
        if abs(pawn[0] - r_q) == abs(pawn[1] - c_q):
            if pawn[0] > r_q and pawn[1] > c_q:
                diag_right_up.append((pawn[0], pawn[1]))
            elif pawn[0] < r_q and pawn[1] > c_q:
                diag_right_down.append((pawn[0], pawn[1]))
            elif pawn[0] > r_q and pawn[1] < c_q:
                diag_left_up.append((pawn[0], pawn[1]))
            elif pawn[0] < r_q and pawn[1] < c_q:
                diag_left_down.append((pawn[0], pawn[1]))



    right_done=False
    left_done=False
    up_done=False
    down_done=False
    diag_right_up_done=False
    diag_right_down_done=False
    diag_left_up_done=False
    diag_left_down_done=False
    

    for position in range(1, n):

        # RIGHT
        new_position = (r_q, c_q + position)
        if right_done:
            pass
        elif new_position in right or new_position[1] > n:
            right_done = True
        else:
            total_attacks += 1

        # LEFT
        new_position = (r_q, c_q - position)
        if left_done:
            pass
        elif new_position in left or new_position[1] < 1:
            left_done = True
        else:
            total_attacks += 1

        # UP
        new_position = (r_q + position, c_q)
        if up_done:
            pass
        elif new_position in up or new_position[0] > n:
            up_done = True
        else:
            total_attacks += 1

        # DOWN
        new_position = (r_q - position, c_q)
        if down_done:
            pass
        elif new_position in down or new_position[0] < 1:
            down_done = True
        else:
            total_attacks += 1

        # DIAG RIGHT UP
        new_position = (r_q + position, c_q + position)
        if diag_right_up_done:
            pass
        elif new_position in diag_right_up or new_position[0] > n or new_position[1] > n:
            diag_right_up_done = True
        else:
            total_attacks += 1

        # DIAG RIGHT DOWN
        new_position = (r_q - position, c_q + position)
        if diag_right_down_done:
            pass
        elif new_position in diag_right_down or new_position[0] < 1 or new_position[1] > n:
            diag_right_down_done = True
        else:
            total_attacks += 1

        # DIAG LEFT UP
        new_position = (r_q + position, c_q - position)
        if diag_left_up_done:
            pass
        elif new_position in diag_left_up or new_position[0] > n or new_position[1] < 1:
            diag_left_up_done = True
        else:
            total_attacks += 1

        # DIAG LEFT DOWN
        new_position = (r_q - position, c_q - position)
        if diag_left_down_done:
            pass
        elif new_position in diag_left_down or new_position[0] < 1 or new_position[1] < 1:
            diag_left_down_done = True
        else:
            total_attacks += 1

    return total_attacks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()
