# https://www.hackerrank.com/challenges/funny-string/problem
# 4 Funny String

#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'funnyString' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def funnyString(s):
    # Write your code here
    w=s[::-1]
    a=[]
    b=[]
    for i in range(1,len(s)-1):
        a.append(abs(ord(s[i])-ord(s[i-1])))
    for i in range(1,len(w)):
        b.append(abs(ord(w[i])-ord(w[i-1])))
    if a==b:
        return "Funny"
    else:
        return "Not Funny"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()
