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
        print "curent position is " + str(currentPosition)
    return currentPosition

rwpos( 40, 4 )


def rwsteps( start, low, hi ):
    currentposition = start
    for i in range (low, hi)
