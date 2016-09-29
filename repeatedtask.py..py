def factorial(n):
    if n == 0:
        return 1
    else:
        answer = factorial(n - 1)
        return n * answer
