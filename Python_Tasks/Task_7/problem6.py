# https://www.hackerrank.com/challenges/pangrams/problem
# 6 Pangrams

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s=s.replace(" ","")
    d='abcdefghijklmnopqrstuvwxyz'
    k=set()
    for i in s.lower():
        if i in d:
            k.add(i)
    if len(k)==26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
