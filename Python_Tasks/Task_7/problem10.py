# https://www.hackerrank.com/challenges/camelcase/problem
# 10 CamelCase

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    k=1
    for i in s:
        if ord(i)>=65 and ord(i)<65+26:
            k+=1
    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
