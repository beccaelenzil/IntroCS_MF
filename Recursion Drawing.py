# python 2
#
# Problem Set 4, Problem 1
#
# name: Matthew Fishbein

from turtle import *
import time

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )




