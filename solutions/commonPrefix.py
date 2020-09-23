def stringSimilarity(s):
    sumlist=[]
    for i in range(len(s)):
        s1 = s[i]   
        t=s1+"$"+s1
        l=0
        r=0
        z=[0]*len(t)
        for i in range(len(t)):
            if(i>r):
                l=r=i
                while(r<len(t) and t[r]==t[r-l]):
                    r+=1
                z[i]=r-l
                r-=1
            else:
                i1=i-l
                if(z[i1]<r-i+1):
                    z[i]=z[i1]
                else:
                    l=i
                    while(r<len(t) and t[r]==t[r-l]):
                        r+=1
                    z[i]=r-l
                    r-=1

        sumlist.append(sum(z[len(s1)+1:]))
    return sumlist
stringSimilarity(['ababaa','bbc'])