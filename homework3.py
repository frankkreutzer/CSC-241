# Problem 4.23
def average():
    '''requests a sentence from the user and returns
       the average length of a word in the sentence'''
    s = input("Enter in a complete sentence: ")
    numWords = len(s.split())
    numchar = len(s) - s.count(' ')
    return numchar / numwords

# Problem 4.24
def cheer(s):
    'prints a cheer for team s'
    print("How do you spell winner?\nI Know, I Know!")
    for chars in s:
         print(chars.upper(), end = " ")
    print('!')
    print("And that's how you spell winner!\nGo " + s + "!")
    


# Problem 4.25
def vowelCount(s):
    'counts and prints the number of occurrences of each vowel in s'
    s = s.lower()
    print("a, e, i, o, and u appear, respectively, ", end = ' ')
    for vowel in 'aeiou':
        print(s.count(vowel), end = ' ')
        if vowel != 'u':
            print(', ', end = ' ')
    print(' times.')

    
    '''numA = s.count('a')
    numE = s.count('e')
    numI = s.count('i')
    numO = s.count('o')
    numU = s.count('u')
    print("a, e, i, o, and u appear, respectively {}, {}, {}, {}, {}".format(numA, numE, numI, numO, numU) + " times.")'''



# Problem 4.26
def crypto(filename):
    '''opens and prints file filename with the modification that
       every occurrence of string 'secret' is replaced with 'xxxxxx'
    '''
    infile = open(filename)
    content = infile.read()
    infile.close()
    print(content.replace('secret', 'xxxxxx'))



# Problem 4.27
def fcopy(original, copy):
    'creates a copy of file original named copy'
    infile = open(original)
    content = infile.read()
    infile.close()
    outfile = open(copy, 'w')
    outfile.write(content)
    file.close()



# Problem 4.29
def stats(filename):
    ' prints the number of lines, words, and characters in file filename'
   '''infile = open(filename)
    lines = infile.readlines()
    infile.seek(0)
    words = infile.read()
    infile.seek(0)
    chars = infile.read()
    infile.seek(0)
    infile.close()
    print("line count:", len(lines))
    print("word count:", len(words.split()))
    print("character counter:", len(chars))'''

    infile = open(filename)
    content = infile.read()
    infile.close()
    print('line count: {}'.format(content.count('\n')+1))
    print('word count: {}'.format(content.count(content.split())))
    print('character count: {}'.format(content.count(len(content))))


# Problem 4.31
def duplicate(filename):
    'checks whether file filename contains duplicate words'
    infile = open(filename)
    content = infile.read()
    infile.close()

    words = content.lower().split()
    
    for word in words:
        if words.count(word) > 1:
            return True
    return False 
