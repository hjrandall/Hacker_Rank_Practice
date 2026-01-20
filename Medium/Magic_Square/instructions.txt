We define a magic square to be an n x n matrix of distinct positive integers from 1 to n squared where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a 3x3 matrix  of integers in the inclusive range [1,9] . We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|. Given , convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2
This took three replacements.

Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

int s[3][3]: a  array of integers
Returns

int: the minimal total cost of converting the input square to a magic square