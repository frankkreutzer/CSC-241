def checkSorted(lst):
    for index in range(1, len(lst)):
        if lst[index] <= lst[index - 1]:
            return False
    return True 



def arithmetic(lst):
    diff = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i + 1] - lst[i] != diff:
            return False 
    return True 



