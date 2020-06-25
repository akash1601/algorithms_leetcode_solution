def lPrefix(strs):
	if not strs: 
            return ''
				
	s1 = min(strs)
	# n print(s1)
	s2 = max(strs)
	# print(s2)
	for i, c in enumerate(s1):
		if c != s2[i]:
			return s1[:i] #stop until hit the split index
	print(str(s1))

lPrefix(["fl","flower","flll"])