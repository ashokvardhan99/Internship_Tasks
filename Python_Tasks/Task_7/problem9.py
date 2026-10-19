# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# 9 Beautiful Binary String
#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#
def beautifulBinaryString(b):
    count = 0
    ans = 0
    while count != 1:
        a = b.find('010')
        if a >= 0:
            b = b[:a+2] + '1' + b[a+3:]
            ans += 1
            count += 0
        else:
            count += 1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    fptr.write(str(result) + '\n')
    fptr.close()
