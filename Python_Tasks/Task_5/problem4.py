# https://www.hackerrank.com/challenges/find-a-string/problem
# 4 Find a String
def count_substring(string, sub_string):
    c=0
    for i in range(len(string)-len(sub_string)+1):
        if sub_string[0]== string[i]:
            a=""
            for j in range(len(sub_string)):
                a = a+string[i+j]
            if a == sub_string:
                c =c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
