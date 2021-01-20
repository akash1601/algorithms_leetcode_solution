def stringCompression(str1):
    ans = []
    count = 1
    for i in range(len(str1) - 1):
        
        if str1[i] != str1[i+1]:
            ans.append(str1[i-1])
            ans.append(count)
            count = 1
        else:
            count += 1
    ans.append(str1[-1])
    ans.append(count)
    str2 = ''.join(map(str, ans))
    print(str2)
    if len(str2) > len(str1):
        return str1
    return str2
stringCompression('aabbccdd')