def cities():
    lst = []
    
    city = input('Enter city: ')

    while city != '':
        lst.append(city)
        city = input('Enter city: ')

    return lst



def cities2():
    lst = []

    while True:
        city = input('Enter city: ')

        if city == '':
            return lst

        lst.append(city)



def cities3():
    lst = []

    while True:
        city = input('Enter city: ')

        if city == '':
            break

        lst.append(city)
    return lst




def before0(table):
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num, end='')
        print()





def ignore0(table):
    for row in table:
        for num in row:
            if num == 0:
                continue
            print(num, end='')
        print() 



