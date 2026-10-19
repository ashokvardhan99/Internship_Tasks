# https://www.hackerrank.com/challenges/mars-exploration/problem
# 3 Mars Exploration

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    b=[]
    for i in range(0,len(s),3):
        b.append(s[i:i+3])
    k=0
    for i in b:
        if i[0]!="S":
            k+=1
        if i[1]!="O":
            k+=1
        if i[2]!="S":
            k+=1
    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
