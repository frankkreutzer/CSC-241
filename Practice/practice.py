import random
def guess(n):
    secret = random.randrange(0, n)
    while True:
        guess = int(input('Enter your guess: '))
        if guess == secret:
            print('You got it!')
            break
        elif guess < secret:
            print('Too low.')
        else:
            print('Too high')


def week():
    days = {'Mo': 'Monday',
            'Tu':'Tuesday',
            'We': 'Wednesday',
            'Th': 'Thursday',
            'Fr': 'Friday',
            'Sa': 'Saturday',
            'Su':'Sunday'}
    abrv = input('Enter a day abreviation: ')
    print(days.get(abrv, ''))
    while True:
        if week() == "":
            break


def names():
    count= {}
    while True:

        name = input('Enter a name:')
        lst = name.split()

        for n in lst:
            count[n] = count.get(n, 0) + 1

        if not lst:
            for n in count:
                if count[n] == 1:
                    print('There is {} student named {}'.format(count[n],n))
                else:
                    print('There are {} students named {}'.format(count[n],n))
            break


def exclamation(s):
    for char in s:
        if char in 'aeiou':
            return s[char]

    

    
def encoding(text):
    print('Char  Decimal  Hex Binary')
    for c in text:
        code = ord(c)
        print('{}    {:7} {:4x}  {:7b}'.format(c, code, code, code))



def lookup(phonebook):
    while True:
        first = input('Enter the first name: ')
        last = input('Enter the last name: ')
        person = (first, last)

        if person in phonebook:
            print(phonebook[person])
        else:
            print('The name you entered in not known.')


def wordcount(text):
    wordList = text.split()
    counters = {}
    for word in wordList:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1

    for word in counters:
        if counters[word] == 1:
            print('{:8} appears {} time'.format(word, \
                                                counters[word]))
        else:
             print('{:8} appears {} times'.format(word, \
                                                counters[word]))



def case(text):
    if text[0].isupper():
        return "Capitalized"
    elif text[0].islower():
        return "Not Capitalized"
    else:
        return "Unknown"
            
