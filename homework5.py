# Problem 5.31
def subsetSum(lst, target):
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst)- 1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    return True
    return False



# Problem 5.32
def fib(n):
    'write docstring here'
    prev = 1
    curr = 1
    
    for i in range(2, n + 1):
        prev, curr = curr, curr + prev
    return curr
        

# Problem 5.38
def collatz(n):
    'write docstring here'
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
    


# Problem 5.42
def primeFac(n):
    'write docstring here'
    #assume n = 12
    #12 % 2 == 0 ---> add 2 to the list
    #12 // 2 = 6 ---> 6 % 2 == 0 ---> add 2 to the list
    #6 // 2 = 3 ---> 3 % 2 == 0: False ---> 3 % 3 == 0 ---> add 3 to the list
    '''i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors'''

    res = []
    div = 2
    while n > 1:
        while n % div ==0:
            res.append(div)
            n //= div
        div += 1
    return res
    



# Problem 5.43
def evenrow(table):
    'write docstring here'
    for i in table:
        if sum(i) % 2 == 1:
            return False
    return True



# Problem 5.46
def inversions(s):
    'write docstring here'
    count = 0
    for i in range(len(s)-1):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                count += 1
        #if s[i] >= s[i+1]:
            #count += 1
    return count




# Problem 5.47
def d2x(n, b):
    'write docstring here'
    '''charSeq = '0123456789ABCDEF'
    if n < b:
        return charSeq[n]
    else:
        return d2x(n//b, b) + charSeq[n%b]'''
    if n == 0:
        return '0'
    res = ''
    while n > 0:
        res = str(n % b) + res
        n //= b
    return res


        
# Problem 5.49
def heron(n, error):
    'write docstring here'
    prev = 1
    new = (1 + n) / 2
    while abs(new - prev) > error:
        prev, new = new, (new + n/new) / 2
    return new
