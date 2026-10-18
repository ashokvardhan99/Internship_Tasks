# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# 15 Set .difference() Operation

eng_num, eng_roll = int(input()), set(input().split())
fre_num, fre_roll = int(input()), set(input().split())
print(len(eng_roll - fre_roll))
