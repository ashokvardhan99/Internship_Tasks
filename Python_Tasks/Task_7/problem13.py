# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# 13 Sherlock and the Valid String

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter

def isValid(s):
    counter_s = Counter(s)
    frequency = Counter(counter_s.values())

    if len(frequency) == 1:
        return "YES"

    if len(frequency) == 2:
        key1, key2 = frequency.keys()
        val1, val2 = frequency[key1], frequency[key2]

        # Case A: one char has freq=1 and it appears once
        if (key1 == 1 and val1 == 1) or (key2 == 1 and val2 == 1):
            return "YES"

        # Case B: frequencies differ by 1 and higher one appears once
        if abs(key1 - key2) == 1 and (frequency[max(key1, key2)] == 1):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
