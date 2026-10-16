# https://www.hackerrank.com/challenges/nested-list/problem
# Nested Lists

if __name__ == '__main__':
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append([name,score])
    g=sorted(set(i[1] for i in s))
    sl=g[1]
    
    n=sorted(i[0] for i in s if i[1]==sl)
    for j in n:
        print(j)
