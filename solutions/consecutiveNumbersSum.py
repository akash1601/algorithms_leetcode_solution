def consecutiveNumbersSum(N):
    ans = 0
    i = 1
    p = N//i
    while p >= (i+1)//2:
        if i % 2 == 0:
            if (p+.5)*i == N:
                ans = ans +1
        else:
            if p * i == N:
                ans = ans +1
        i = i+1
        p = N//i
        
    return ans
consecutiveNumbersSum(9)