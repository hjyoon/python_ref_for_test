# Nested Recursion Ex
def ackermann(x, y):
    if x == 0:
        return y + 1
    if x < 0 or y < 0:
        return -1
    elif x > 0 and y == 0:
        return ackermann(x-1, 1)
    else:
        return ackermann(x-1, ackermann(x, y-1))


print(ackermann(3, 2))


# Tail Recursion Ex
def fibnum2(n, x, y):
    if n == 1:
        return y
    else:
        return fibnum2(n-1, y, x+y)


print(fibnum2(6, 1, 0))


# Binary Recursion Ex
def fibnum(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    return fibnum(n-1) + fibnum(n-2)


print(fibnum(6))


# Linear Rescursion Ex
def fact(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))


# Mutual Recursion Ex
def IsOddNumber(n):
    if n == 0:
        return False
    else:
        return IsEvenNumber(n-1)


def IsEvenNumber(n):
    if n == 0:
        return True
    else:
        return IsOddNumber(n-1)


print(IsOddNumber(10))
print(IsEvenNumber(10))
