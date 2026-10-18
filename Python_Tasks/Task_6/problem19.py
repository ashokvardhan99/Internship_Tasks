# https://www.hackerrank.com/challenges/most-commons/problem
# 19 Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    dic = {}
    for char in s:
        dic[char] = dic.get(char, 0 ) + 1
    count = 0
    final = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
    for c in final:
        if count < 3:
            print(*c)
            count += 1
