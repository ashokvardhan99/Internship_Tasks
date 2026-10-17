# https://www.hackerrank.com/challenges/swap-case/problem
# 10 Swap Case

def swap_case(s):
    h= ""
    for i in s:
        if ord(i)<=90 and ord(i) >=65:
            h=h+chr(ord(i)+32)
        elif ord(i)>=97 and ord(i)<=122:
            h=h+chr(ord(i)-32)
        else:
            h=h+i
    return h

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

