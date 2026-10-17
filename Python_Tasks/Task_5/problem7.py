# https://www.hackerrank.com/challenges/symmetric-difference/problem
# 7 Symmetric Difference

m=int(input())
p=set(map(int,input().split()))
n=int(input())
s=set(map(int,input().split()))

fs= sorted(p.symmetric_difference(s))
for i in fs:
    print(i)
