# https://www.hackerrank.com/challenges/reduced-string/problem
# 20 Super Reduced String

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    stack = []
    
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    
    if not stack:
        return "Empty String"
        
    return "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
