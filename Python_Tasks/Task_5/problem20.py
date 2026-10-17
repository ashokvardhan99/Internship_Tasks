# https://www.hackerrank.com/challenges/piling-up/problem
# 20 Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    possible = True
    while cubes:
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()
        if cube > top:
            possible = False
            break
        top = cube
    print("Yes" if possible else "No")
