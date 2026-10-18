# https://www.hackerrank.com/challenges/designer-door-mat/problem
# 10 Designer Door Mat

N, M = (int(_) for _ in input().split(' '))
#patterns
p1 = '.|.'
bg = '-'
msg = 'WELCOME'

#printing logo
for i in range(1, N//2+1):
    block = p1*(i*2-1)
    print(block.center(M, bg))
print(msg.center(M, bg))
for i in range(N//2, 0, -1):
    block = p1*(i*2-1)
    print(block.center(M, bg))
