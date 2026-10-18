# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# 1 Set .symmetric_difference() Operation

eng, eng_roll = int(input()), set(input().split())
fre, fre_roll = int(input()), set(input().split())
print(len(eng_roll ^ fre_roll))
