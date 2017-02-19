def postal(first, last, address, city, state, zipcode):
    'print postal mailing address'
    print("{} {}\n{}\n{}, {} {}".format((frist), (last), (address), (city), (state), (zipcode)))



def evens(n):
    'return the list of the first n positive even numbers'
    res = []
    for i in range(2, 2 * n + 1, 2):
        res.append(i)
    return res



def lastChars(filename, i):
    'return last i characters of file filename'
    infile = open(filename)
    content = infile.read()
    infile.close()

    return content[-i:]
    

    
 
def noVowel(s):
    'return True if string s contains no vowel, False otherwise'
    for char in s:
        if char.lower() in 'aeiou':
            return False
    return True



def emphasize(s):
    'return copy of string s with blank spaces inserted between adjacent characters'
    return (s.replace('', ' ')[1:-1])
