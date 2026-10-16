# https://www.hackerrank.com/challenges/find-a-string/problem

# Find a String

for i in range(len(string)-len(sub_string)+1):
  if sub_string[0] == string[i]:
    a = ""
    for j in range(len(sub_string)):
      a = a + string[i+j]
    if a == sub_string:
      count = count + 1
