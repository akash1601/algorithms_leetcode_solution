def countAndSay(n):
    if n == 1: 
        return "1"
    s = self.countAndSay(n-1)
    i, ch, tmp = 0, s[0], ''
    for j in range(1, len(s)):
        if s[j] != ch:
            tmp += str(j-i) + ch
            i, ch = j, s[j]
    tmp += str(len(s)-i) + ch
    return tmp