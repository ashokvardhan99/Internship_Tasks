# https://www.hackerrank.com/challenges/word-order/problem

# 9 Word Order

n=int(input())
d={}
for i in range(n):
    word=input()
    d[word]=d.get(word,0)+1
    
print(len(d))
print(*d.values())
