# python 2
#
# Homework 3, Problem 1
# Loops!
#
# Name:
#

def fac(n):
    """ loop-based factorial function
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests: run by pressing the Run button above

print "fac(0): should be 1 == ", fac(0)
print "fac(5): should be 120 == ", fac(5)

def power(b,p):
    result = 1
    for x in range(p):
        result = result*b
        print result
    return result


'''
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)
'''

def mult(m,n):
    result = 0
    if n>= 0:
        for x in range(n):
            result = result + m
            #print result
        return result
    else:
        for x in range(-1*n):
            result = result + m
            #print result
        return result*-1


print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)


print mult(6,7)


def count_evens():
    result =
    if



print "count_evens([2, 1, 2, 3, 4], 3 == ", count_evens([2, 1, 2, 3, 4])
print "count_evens([2, 2, 0]), 3 == ", count_evens([2, 2, 0])
print "count_evens([1, 3, 5]), 0 == ", count_evens([1, 3, 5])




print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])
