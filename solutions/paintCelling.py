def generateS(n, s0, k, b, m):
    S = [s0] + [0]*(n-1)
    for i in range(1, n):
        S[i] = S[i-1] + 1 + (k*S[i-1] + b)%m
    return S

def variantsCount(n, s0, k, b, m, a):
    S = generateS(n, s0, k, b, m)
    i, j = 0, n-1
    result = 0
    while i < n and j > -1:
        if S[i] * S[j] <= a:
            result += j + 1
            i += 1
        else:
            j -= 1
    return result