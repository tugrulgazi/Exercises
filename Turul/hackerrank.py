# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 03:06:41 2020

@author: Turul
"""
#!/bin/python3



#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))


    
def diagonalDifference(arr):
    # Write your code here

    right = 0
    left = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                right += arr[i][j]
    for i in range(n):
        arr[i]=reversed(arr[i])
    for i in range(n):
        for j in range(n):
            if i==j:
                left += arr[i][j]
    return abs(right-left)
    
result = diagonalDifference(arr)

    

    

    

    

