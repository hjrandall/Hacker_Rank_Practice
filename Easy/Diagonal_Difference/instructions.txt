Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15.
The right-to-left diagonal = 3+5+9=17.
Their absolute difference is |15-17|=2.

Function description

Complete the diagonal difference function with the following parameter:

:int arr[n][m] a 2-D array of integers

Return

int: the absolute difference in sums along the diagonals
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row,arr[i] , and consists of n space-separated integers arr[i[j]].

Constraints
    -100<=arr[i][j]<=100

Sample Input

STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: .

The secondary diagonal is:
11+5-12=4

     4
   5
10
Sum across the secondary diagonal: 
4+5+10=19
Difference: |4-19|=15

Note: |x| is the absolute value of x.