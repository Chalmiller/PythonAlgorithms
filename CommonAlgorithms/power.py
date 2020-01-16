def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def partial_power(x, n):
    if n == 0:
        return 1
    else:
        partial = partial_power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result