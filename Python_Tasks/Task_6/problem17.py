# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# 17 Check Strict Superset

set_a = set(input().split())
result = set()
for _ in range(int(input())):
    other = set(input().split())
    result.add(set_a.issuperset(other) and len(set_a) > len(other))
print(all(result))
