# python 2
#
# Game of Life
#
# Name: Molly and Matthew
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
        #print row
    return row

createOneRow(10)

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        # create a row with width 'width' using the function createOneRow
        r = createOneRow(width)

        #add that row to your 2D matrix A
        A += [r]
    return A

A = createBoard(7, 6)
print A

def printBoard(A):
    for row in A:
        #print "row: ",row
        line = ''
        for col in row:
            #print "col:", col
            line += str(col)
        print line

#A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

printBoard(A)

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(1, height-1):
        for col in range( 1, width -1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A




