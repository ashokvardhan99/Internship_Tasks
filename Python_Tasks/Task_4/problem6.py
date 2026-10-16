# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())

sm= sorted(set(arr))
print(sm[-2])
