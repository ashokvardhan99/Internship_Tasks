# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sm= sorted(set(arr))
    print(sm[-2])

