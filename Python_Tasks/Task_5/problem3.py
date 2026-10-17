# https://www.hackerrank.com/challenges/python-mutations/problem
# 3 Mutations

def mutate_string(string, position, character):
    h=string[:position]+character+string[position+1:]
    return h

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
