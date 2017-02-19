from math import sqrt
def qsolver(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return 'No roots'
    if d == 0:
        return -b/(2*a)
    return ((-b - sqrt(d))/(2*a), (-b + sqrt(d))/(2*a))

def phone(number):
    mapping = '22233344455566677778889999'
    res = ''
    for c in number:
        position = ord(c.upper()) - ord('A')
        res += mapping[position]
    return res


def approxPIsquared(error):
    prev = 8
    curr = 8 + 8/3**2
    i = 5
    while curr - prev > error:
        prev, curr = curr, curr + 8/i**2
        i += 2
    return curr



from random import randrange
def yahtzee():
    rolls = [0,0,0,0,0]
    for i in range(5):  
        rolls[i] = randrange(1,7)
    for i in range(2):
        print('You have {}, {}, {}, {}, and {}'.format(rolls[0], rolls[1], rolls[2], rolls[3], rolls[4]))
        choices = input('What dice do you want to save?').split(',')
        for i in range(5):
            if str(i) not in choices:
                rolls[i] = randrange(1,7)
    print('You have {}, {}, {}, {}, and {}'.format(rolls[0], rolls[1], rolls[2], rolls[3], rolls[4]))
    print('Write your score.')


    
    
