# https://www.hackerrank.com/challenges/collections-counter/problem
# Collections.Counter()

from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))

N = int(input())
total_money = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        total_money += price
        shoe_sizes[size] -= 1

print(total_money)
