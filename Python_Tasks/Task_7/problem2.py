# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# 2 The Captain's Room

s=int(input())
w=list(map(int,input().split()))
q=set()
k=set()
for i in w:
    if i in q:
        k.add(i)
    else:
        q.add(i)
for i in q:
    if i not in k:
        print(i)
