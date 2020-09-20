def binary(s,x):
    count = 0
    for i in range(len(s)):
        a = int(s[i],2)
        if a%int(x) == 0:
            count +=1
    return count
text = "3,110100000101,100010101110,100010110001"
s= text.split(',')
print(s)
binary(s[1:],s[0])