def acronym(s):
    words = s.split()
    res = ''
    for w in words:
        res += w[0].upper()
    return res
         
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def divisor(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res += [i]       #same as res.append(i)
    return res
