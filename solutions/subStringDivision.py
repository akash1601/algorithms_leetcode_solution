def subStringDivision(n,k):
    s = str(n)
    count = 0
    str1 = str()
    for i in range(0,len(s) - k+1):
        str1 = s[i:i+k]
        print(str1)
        if (n % int(str1) == 0):
            count = count +1
            
    return count
subStringDivision(120,2)

