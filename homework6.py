# Problem 5.33
def mystery(n):
    'returns mystery number'
    count = 0
    while n > 1:
        n = n // 2
        count += 1   
    return count

    
# Problem 5.48
def sublist(lst1, lst2):
    'checks whether list lst1 is a sublist of list lst2'
    i, j = 0, 0
    while i < len(lst1):
        while j < len(lst2) and lst2[j] != lst1[i]:
            j += 1
        if j == len(lst2):
            return False 
        i += 1
    return True 


# Problem 3
def gnome():
    'solves gnome problem'
    infile = open('gnome.txt')
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline()
        values = line.split()
        first, second, thrid, = int(value[0]), int(value[1]), int(value[2])
        if first < second < third or first >= second >= third:
            print('Ordered')
        else:
            print('Unordered')
    infile.close()

            
# Problem 4
def speed():
    'solves speed problem'
    infile = open('speed.txt')
    while True:
        n = int(infile.readline())
        if n == -1:
            break
        res = 0
        t = 0
        for i in range(n):
            values = infile.readline().split()
            speed, tnew = int(values[0]), int(values[1])
            res += (tnew - t) * speed
            t = tnew
        print('{} miles'.format(res))
    infile.close()
        

# Problem 5
def rrot(rot, s):
    'returns reverse rotation by rot of s'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    res = ''
    for c in s:
        x = alphabet.index(c)
        res += alphabet[(x + rot) % len(alphabet)]
        copy = res[::-1]
    return copy



