def countPowerNumbers(l,r):
    if r<=2: return 0

    spf = [i for i in range(r+1)]
    spf[0] = 1
    mxn = int(r**.5)+1
    for i in range(4,mxn+1,2): spf[i]=2
    for i in range(3,int(mxn**.5)+1):
        if spf[i]==i:
            for j in range(i*i, mxn+1, i):
                if spf[j]==j: spf[j]=i
    primePowers = []
    for i in range(2,mxn):
        if spf[i]==i:
            x = i**2
            while x<=r:
                primePowers.append(x)
                x*=i
    res = 0
    for i in range(len(primePowers)):
        for j in range(i,len(primePowers)):
            summ = primePowers[i]+primePowers[j]
            res += (l<=summ<=r)
    return res

l,r = 20,25
print(countPowerNumbers(l,r))