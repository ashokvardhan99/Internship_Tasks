## https://www.hackerrank.com/challenges/py-if-else/problem
# Python If-Else
h=int(input())

n=eval(input())
if n%2!=0:
    print('Weird')
elif 2<n<5 or n>20:
    print('Not Weird')
else:
    print('Weird')
