def innerProduct(x, y):
    res = 0
    for index in range(len(x)):
        res += x[index]*y[index]
    return res


def digitsum(n):
    res = 0
    for c in str(n):
        res += int(c)
    return res


def digitsum(n):
    res = 0
    while n > 0:
        res += n%10
        n //= 10
    return res



import string
def wordcount(filename):
    infile = open(filename)
    content = infile.read().lower()
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    content = content.translate(table)
    words = content.split()
    d = {}
    for w in words:
        if len(w) > 2:
            if w not in d:
                d[w] = 1
            else: # w in d
                d[w] += 1
    for w in d:
        print('{:15}{:4}'.format(w, d[w]))


import random
def manhattan():
    table = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    x,y = 10,10
    while 0<=x<=20 and 0<=y<=20:
        table[x][y] += 1
        d = random.choice(['N', 'S','E','W'])
        if d == 'N':
            y += 1
        elif d == 'S':
            y -= 1
        elif d == 'E':
            x +=1
        else:
            x -= 1
    for row in table:
        print(row)