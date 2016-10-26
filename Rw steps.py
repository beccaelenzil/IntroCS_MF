import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])



def rwpos(start, nsteps):
    currentPosition = start
    for i in range (0, nsteps):
        currentPosition = currentPosition + rs()
        print "current position is " + str(currentPosition)
    return currentPosition

#rwpos( 40, 4 )


def rwsteps( start, lo, hi ):
    currentposition = start
    count = 0
    while currentposition < hi and currentposition > lo:
        right = currentposition - lo - 1
        left = hi - currentposition
        print "|"+right*" "+"S"+left*" "+"|"
        currentposition += rs()
        count += 1
    return count


#print rwsteps(10,5,15)


def rwposPlain(start, nsteps):
    currentPosition = start
    for i in range (0, nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition

print rwposPlain( 20, 4 )

rwsteps(5,0,10)
'''
def ave_signed_displacement( numtrials ):
    for i in range(numtrials):
        L[]
        for i in range(numtrials):
            currentPos = rwPosPlain(0,100)
            L.append(currentPos)
            return

'''
