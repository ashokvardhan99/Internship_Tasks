# https://www.hackerrank.com/challenges/py-if-else/problem
# 1 Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys


n=eval(input())
if n%2!=0:
    print('Weird')
elif 2<n<5 or n>20:
    print('Not Weird')
else:
    print('Weird')

