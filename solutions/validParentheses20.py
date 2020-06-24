def validP(s):
	while '[]' in s or '{}' in s or '()' in s:
		s = s.replace('[]','').replace('{}','').replace('()','')
	print(len(s))
validP("([)")