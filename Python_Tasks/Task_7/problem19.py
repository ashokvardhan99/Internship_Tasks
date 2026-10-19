# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# 19 Weighted Uniform Strings

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    
    n = set()
    c = 0
    repeat_multiplier = 1
    while c < len(s):
        if c > 0 and s[c - 1] == s[c]:
            repeat_multiplier += 1
        else:
            repeat_multiplier = 1
        weight = (ord(s[c]) - 96) * repeat_multiplier
        n.add(weight)
        c += 1
    result = []
    for i in queries:
        if i in n:
            result.append("Yes")
        else:
            result.append("No")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
