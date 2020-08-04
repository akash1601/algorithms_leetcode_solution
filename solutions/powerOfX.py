def powerOfX(x,n):
    if not n:
        return 1
    if n < 0:
        return 1/powerOfX(x,-n)
    if n%2:
        return powerOfX(x,n-1)
    return powerOfX(x*x,n/2)
powerOfX(2,10)