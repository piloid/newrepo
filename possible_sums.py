from itertools import *

def digits(num):
    b = str(num)
    s = []
    for i in range(len(b)):
        print(b[i])
        s.append(int(b[i]))
    k = []
    for j in combinations(s, 2):
        k.append(sum(j))
    return k
