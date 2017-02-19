def print2D(table):
    for row in table:
        for i in row:
            print(i, end = ' ')
        print()


def incr2D(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] += 1
