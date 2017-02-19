def nested(n):
    for j in range(n):
        for i in range(n):
            print (i, end = ' ')
        print()        

def nested2(n):
    for j in range(n):
        for i in range(j + 1):
            print (i, end = ' ')
        print()        

def nested3(n):
    for j in range(n):
        for i in range(n - j):
            print (i, end = ' ')
        print()   
    for j in range(n):
        for i in range(j + 1):
            print (i, end = ' ')
        print()


def inBoth(lst1, lst2):
    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                return True
    return False


def pairSum(lst, target):
    for i in range(len(lst)-1):    #all possible left indexes
        for j in range(i+1, len(lst)):    #all possible right indexes
            if lst[i] + lst[j] == target:
                print(i, j)
    
