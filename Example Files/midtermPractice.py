def test(n):
    if n < 0:
        print("Negative")
    elif n == 0:
        print("Zero")
    else:
        print("Postitive")



def mult3(lst):
    for num in lst:
        if num % 3 == 0:
            print(num)



def vowels(s):
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            print(i)



def indexes(s, char):
    res = []
    for i in range(len(s)):
        if char == s[i]:
            res.append(i)
    return res


def doubles(l):
    for i in range(1, len(l) - 1):
        if l[i] * 2  == l[i + 1]:
            print(l[i + 1])



def isodd(n):
    if n % 3 == 0:
        print("odd")
    else:
        print("even")


def average(lst):
    for lsts in lst:
        print(sum(lsts)/len(lsts))







