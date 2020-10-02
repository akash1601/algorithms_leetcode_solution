def isAnagram(s, t):
     #   return sorted(s) == sorted(t)
    
        for l in string.ascii_lowercase:

            if s.count(l)!=t.count(l):
                return False
        return True