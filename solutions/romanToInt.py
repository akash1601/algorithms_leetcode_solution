def romanToInt(strs):
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(len(strs)-1):
		if roman[strs[i]] < roman[strs[i+1]]:
			z -= roman[strs[i]]
		else:
			z += roman[strs[i]]
	print(strs[-1])
	print(z+roman[strs[-1]])

romanToInt("IV")