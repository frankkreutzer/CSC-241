def negative(lst):
    '''for i in range(len(lst)):
        if lst[i] < 0:
            return i'''

    index = 0
    while index < len(lst) and lst[index] >= 0:
        index += 1     #if value at index is >= 0 increment to the next index
    if index == len(lst):
        return -1
    else:
        return index 
        
    
def fib(bound):
    prev = 1
    curr = 1
    while curr <= bound:
        prev, curr = curr, curr + prev     #the new prev becomes old curr and the new curr becomes the sum of the old prev and curr
    return curr


def approxE(error):
    prev = 1
    curr = 2
    i = 2
    while curr - prev >= error:
        prev, curr = curr, curr + 1/factorial(i)
        i += 1
    return curr
