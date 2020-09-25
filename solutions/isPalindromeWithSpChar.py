def isPalindrome(s) :
        s1 = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                s1.append(i)
        s2 = ''.join(s1)
        return s2 == s2[::-1]