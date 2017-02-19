from random import randrange
def simul(n):
    rounds = 0
    cntp1 = 0
    cntp2 = 0
    # Consider Rock = 0, Paper = 1, and Scissors = 2
    while rounds < n:
        play1 = randrange(0, 3)
        play2 = randrange(0, 3)
        rounds += 1
        if (play1 == 0 and play2 == 2) or (play1 == 2 and play2 == 1) or (play1 == 1 and play2 == 0):
            cntp1 += 1
        elif (play1 == 2 and play2 == 0) or (play1 == 1 and play2 == 2) or (play1 == 0 and play2 == 1):
            cntp2 += 1
    if cntp1 > cntp2:
        print('Player 1')
        print('P1: ' + str(cntp1) + '\n' + 'P2: ' + str(cntp2) + '\n' + 'Ties: ' + str(100 - (cntp1 + cntp2)))
    elif cntp2 > cntp1:
        print('Player 2')
        print('P1: ' + str(cntp1) + '\n' + 'P2: ' + str(cntp2) + '\n' + 'Ties: ' + str(100 - (cntp1 + cntp2)))
    else:
        print('Tie')
        print('P1: ' + str(cntp1) + '\n' + 'P2: ' + str(cntp2) + '\n' + 'Ties: ' + str(100 - cntp1 + cntp2))


simul(100)
