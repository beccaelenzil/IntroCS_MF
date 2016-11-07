#https://trinket.io/library/trinkets/3b87f47b58
def fib(n):
    if n == 0:
        return 1
    if n ==1:
        return 1
    if n > 1:
        return fib(n-2)+fib(n-1)


def fibIter(n):
    fibseq = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            fibseq.append(fibseq[i-1]+fibseq[i-2])
            print fibseq[-1]
        return fibseq[-1]


#There were a number of mismatching cases that made this not run. I fixed them for you.
def listReverseIter(l):
    K = []
    for i in range (len(l)-1,-1,-1):
        K.append(l[i])
    return K

def listReverse(L):
    if len(L)== 1:
        return L
    #else:
    return L[-1] + listReverse(L[0:-1])




    
