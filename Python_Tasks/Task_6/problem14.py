# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# 14 Set .intersection() Operation

english, roll_e = int(input()), set(input().split())
french, roll_f = int(input()), set(input().split())
print(len(roll_e & roll_f))
