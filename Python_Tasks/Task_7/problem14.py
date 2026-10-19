# https://www.hackerrank.com/challenges/anagram/problem
# 14 Anagram
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1
    s1 = list(s[:len(s) // 2])
    s2 = list(s[len(s) // 2:])
    letters = set(s1 + s2)
    same = 0
    for letter in letters:
        same += min(s1.count(letter), s2.count(letter))
    return (len(s1) + len(s2) - 2 * same) // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

