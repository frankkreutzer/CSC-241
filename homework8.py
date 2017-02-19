# Problem 6.31
from random import randrange
def craps():
    'simulates a game of craps'
    roll = randrange(1, 7) + randrange(1, 7)
    if roll in (7, 11):
        return 1
    elif roll in (2, 3, 12):
        return 0
    return rollForPoint(roll)

def rollForPoint(originalRoll):
    while True:
        roll = randint(1, 7) + randint(1, 7)
        if roll == originalRoll:
            return 1
        elif roll == 7:
            return 0


def testCraps(n):
    'simulates n games of craps and returns the fraction of games won'
    count = 0
    for i in range(n):
        count += craps()
    return count/n


# Problems 6.35 and 7.17
from random import randrange
def game(n):
    'an app to teach simple arithmetic'
    questions = 0
    correctCount = 0
    while questions < n:
        questions += 1
        n1 = randrange(10)
        n2 = randrange(10)
        ans = n1 + n2
        print('{} + {} = ?'.format(n1, n2))

        while True:
            try:
                userAns = int(input('Enter answer: '))
                break
            except:
                print('Please write your answer using digits. Try again!')

        if ans == userAns:
            correctCount += 1
            print('Correct!')
        else:
            print('Incorrect.')

    print('You got {} correct answers out of {}'.format(correctCount, n))


# Problem 7.19
def inValues():
    '''interactive function that requests non-zero numbers from the user;
       when the user enters 0, the sum of the numbers input is printed.
       The function terminates when the user enters two invalid inputs
       in a row.'''
    res = 0
    error = 0
    while True:
        try:
            n = float(input('Please enter a number: '))
            errors = 0
        except:
            if errors < 1:
                print('Error. Please re-enter the value.')
                errors += 1
                continue
            print("Two errors in a row. Quitting...")
            break
        res += n
