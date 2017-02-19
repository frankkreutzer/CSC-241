# Problem 5.15
# counter loop pattern
def vowels(s):
    'prints the indexes of all vowels in string s'
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":  
            print(i)


# Problem 5.17
# counter loop pattern
def doubles(l):
    '''prints integers in list l that are exactly twice
       the previous integer in the list'''
    for i in range(1, len(l) - 1):
        if l[i] * 2  == l[i + 1]:
            print(l[i + 1])
    



# Problem 5.18
# iteration and accumulator loop patterns
def four_letter(lst):
    'returns list of 4-letter words in list of strings lst'
    res = []
    for w in lst:
        if len(w) == 4:
            res.append([w])
    return res




# Problem 5.23
def pay(rate, hours):
    '''returns wage based on rate and hours

       Any hours beyond 40 but less than or equal 60 are paid at
       1.5 times the regular hourly wage. Any hours beyond 60 are
       paid at 2 times the regular hourly wage'''
    if 40 < hours <= 60:
        return 40 * rate + rate * (hours - 40) * 1.5
    elif hours > 60:
        return 40 * rate + 20 * 1.5 + (hours - 60) * rate * 2
    else:
        return rate * hours



# Problem 5.26
def rps(play1, play2):
    '''takes choices ('R', 'P', or 'S') of player 1 and 2,
       and returns -1 if player 1 wins, 1 if player 2 wins,
       or 0 if there is a tie'''
    if (play1 == 'R' and play2 == 'S') or (play1 == 'S' and play2 == 'P') or (play1 == 'P' and play2 == 'R'):
        return -1
    elif (play1 == 'S' and play2 == 'R') or (play1 == 'P' and play2 == 'S') or (play1 == 'R' and play2 == 'P'):
        return 1
    else:
        return 0
    





# Problem 5.28
def geometric(lst):
    'checks whether the integers in list lst form a geometric sequence'
    
    '''Checking the index before'''
    ratio = lst[i]/lst[0]
    for i in range(2, len(lst)):
        if lst[i]/lst[i - 1] !=  ratio:
            return False
    return True

    '''Checking the index after'''
    ratio = lst[i]/lst[0]
    for i in range(1, len(lst) - 1):
        if lst[i + 1]/lst[i] != ratio:
            return False
    return True 




# Problem 5.30
def many(filename, n):
    import string
    'prints the number of words of length 1, 2, 3, and 4 in file filename'
    '''infile = open(filename)
    content = infile.read()
    infile.close() 
    table = str.maketrans(string.puncuation,, len(string.punctuation * ' ')
    content = content.translate(table)                      
    words = content.split()'''
                          
    count1, count2, count3, count4 = 0, 0, 0, 0

    for word in words:
        if len(word) == 1:
            count1 += 1
        elif len(word) == 2:
            count2 += 1
        elif len(word) == 3:
            count3 += 1
        elif len(word) == 4:
            count4 += 1
    print(" Words of length 1 : {}\n".format(count1),"Words of length 1 : {}\n".format(count2),"Words of length 1 : {}\n".format(count3), "Words of length 1 : {}\n".format(count4))


    counter = 4 * [0]
    for word in words:
        if len(word) <= n:
           counter[len(word) - 1]
    for i in range(n):
        print("Words of length {}: {}".format(i + 1, counter[i]))
    

# Problem 5.34   
def statement(lst):
    '''returns a list of two numbers; the first is the sum of the
       positive numbers (deposits) in list lst, and the second is
       the sum of the negative numbers (withdrawals)'''
    '''sums = [0, 0] 
    for n in lst:
        sums[n < 0] += n
    return sums'''

    deposite, withdrawl = 0, 0
    for n in lst:
        if n < 0:
            withdrawl += n
        else:
            deposite += n
    return [deposite, withdrawl]


# Problem 5.41
def poly(a, x):
    '''a is a list of coefficients a0, a1, a2, a3, . . . , an of
       a polynomial p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n;
       function computes and returns p(x)'''
    '''total, power = 0, 0
    for coeff in a:
        total += (x**power) * coeff
        power += 1
    return total'''

    res = 0
    for i in range(len(a)):
        res += a[i] * x**i
    return res


