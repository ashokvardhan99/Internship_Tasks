# https://www.hackerrank.com/challenges/string-validators/problem
# String Validators

s = input()
print (s.isalnum())
print(any(char.isalpha() for char in s))
print (any(char.isdigit()for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))
