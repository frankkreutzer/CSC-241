#
# NOTE:
# 
# A function must have a code block otherwise
# Python will complain. For that reason I put
# a pass Python statement where the code block
# should be. The pass statement does absolutely
# nothing. You should replace the pass statement
# with your function implementation

def forLoop():
    ''' printing numbers 5, 9, 13, 17, and 21
    one per line
    
    usage:
    >>> forLoops()
    5
    9
    13
    17
    21

    '''
    for i in range(5, 24, 4):
        print(i)


# Problem 3.34
def pay(wage, hours):
    '''return employees pay; overtime (beyond 40 hours)
       is paid at 1.5 times the regular hourly wage'''  
    if hours <= 40:
        return wage * hours
    else:
        return 40 * wage + (hours - 40) * wage * 1.5
        




# Problem 3.35
def prob(n):
    'return probability of getting n heads in a row'
    if n >= 1:
        return (0.5)**n
    else:
        return 0




# Problem 3.37
import math
def points(x1, y1, x2, y2):
    '''print slope and length of line segment passing
       through points (x1,y1) and (x2,y2)'''
    slope = (y2 - y1) / (x2  - x1)
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if x1 == x2:
        print('Infinite')
    else:
        print('The slope is ' + slope + ' and the distance is ' + length)
    



# Problem 3.38
def abbreviation(day):
    'return two-letter abbreviation of day of the week'
    return day[:2]




# Problem 3.39
def collision(x1, y1, r1, x2, y2, r2):
    '''checks whether two circles with centers (x1,y1) and (x2,y2)
       and radii r1 and r2, respectively, intersect'''
    import math
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2) <= r1 + r2




# Problem 3.40
def partition(lst):
    '''prints the names in list lst that start
       with a letter between and including A and M'''
    for word in lst:
        if word[0] in 'ABCDEFGHIJKLM':
            print(word)




# Problem 3.41
def lastF(first, last):
    '''prints the full last name, and the first
       inital of the first name'''
    print(last + ', ' + first[0] + '.')




# Problem 3.42
def avg(lst):
    '''lst is a list that contains lists of numbers; the
       function prints, one per line, the average of each list'''
    for lsts in lst:
        print(sum(lsts)/len(lsts))




# Problem 3.43
import math
def hit(xc, yc, rc, xp, yp):
    ''' check whether point (xp, yp) is inside circle
        with center (xc, yc) and radius rc'''
    d = math.sqrt((xc-xp)**2 + (yc - yp)**2)
    return d <= rc
