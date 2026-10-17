# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# 2. String Split and Join

def split_and_join(line):
    return line.replace(" ","-")
    w=line.split()
    n="-".join(w)
    return n


if __name__ == '__main__':
