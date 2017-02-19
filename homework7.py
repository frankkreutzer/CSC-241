
# Exercise 6.12
def letter2number(lgrade):
    'returns the number grade corresponding to the letter grade lgrade'
    grades = {'A+': 4.3, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7,
              'C+': 2.3, 'C': 2, 'C-': 1.7, 'D+': 1.3, 'D': 1, 'D-': 0.7,
              'F+': 0.3, 'F': 0}
    return grades[lgrade]


# Exercise 6.17
def hexASCII():
    '''prints correspondence between the lowercase characters in the
       alphabet and the hexadecimal representation of their ASCII code'''
    print("a:{} b:{} c:{} d:{} e:{} f:{} g:{} h:{} i:{} j:{} k:{} l:{} m:{} n:{} o:{} p:{} q:{} r:{} s:{} t:{} u:{} v:{} w:{} x:{} y:{} z:{}".format(format(ord('a'), 'x'), format(ord('b'), 'x'), format(ord('c'), 'x'), format(ord('d'), 'x'), format(ord('e'), 'x'), format(ord('f'), 'x'), format(ord('g'), 'x'), format(ord('h'), 'x'), format(ord('i'), 'x'), format(ord('j'), 'x'),
                                                                                                                                                     format(ord('k'), 'x'), format(ord('l'), 'x'), format(ord('m'), 'x'), format(ord('n'), 'x'), format(ord('o'), 'x'), format(ord('p'), 'x'), format(ord('q'), 'x'), format(ord('r'), 'x'), format(ord('s'), 'x'), format(ord('t'), 'x'),
                                                                                                                                                     format(ord('u'), 'x'), format(ord('v'), 'x'), format(ord('w'), 'x'), format(ord('x'), 'x'), format(ord('y'), 'x'), format(ord('z'), 'x')))

# Exercise 6.18
import random
def coin():
    '''returns 'Heads' or 'Tails' with equal probability'''
    coin = ['Heads', 'Tails']
    random.shuffle(coin)
    return random.choice(coin)


# Problem 6.22
def mirror(word):
    '''returns mirror image of word but if it can be represented
       using letters in the alphabet'''
    mirror = {'b': 'd', 'd': 'b', 'o': 'o', 'p': 'q',
              'q': 'p', 'v': 'v', 'w': 'w', 'x': 'x'}
    res = ''
    for c in word:
        if c in mirror:
            res = d[c] + res
        elif c in 'owvx':
            res = c + res
        else:
            return "INVALID"
    return res 



# Problem 6.23
import string
def scaryDict(filename):
    infile = open(filename)
    content = infile.read().lower()
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    content = content.translate(table)
    words = content.split()
    words = list(set(words)).sort()
    outfile = open('dictionary.txt', 'w')
    for w in words:
        print(w)
        outfile.write(w + '\n')
    outfile.close()



# Problem 6.30
import random
def simul(n):
    rounds = 0
    count1 = 0
    count2 = 0
    #Consider Rock = 0, Paper = 1, and Scissors = 2
    while rounds < n:
        play1 = random.randrange(0, 3)
        play2 = random.randrange(0, 3)
        rounds += 1
        if (play1 == 0 and play2 == 2) or (play1 == 2 and play2 == 1) or (play1 == 1 and play2 == 0):
            count1 += 1
        elif (play1 == 2 and play2 == 0) or (play1 == 1 and play2 == 2) or (play1 == 0 and play2 == 1):
            count2 += 1
    if count1 > count2:
        print('Player 1')
    elif count2 > count1:
        print('Player 2')
    else:
        print('Tie')




# Problem 6.33
from random import randrange
def diceprob(r):
    '''simulates repeated rolls of a pair of dice until
       100 rolls of r have been obtained; the number of
       rolls is then printed'''
    total_count = 0
    count = 0

    while count < 100:
        roll = random.randrange(1, 7) + random.randrange(1, 7)
        total_count += 1
        if roll == r:
            count += 1
    print("It took {} rolls to get 100 rolls of {}".format(total_count, r))
