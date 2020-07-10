def group(strs):

	x = {}
	for string in strs:
		s = ''.join(sorted(string))

		if s in x:
			x[s].append(string)
		else:
			x[s] = [string]

	return x.values


group(["eat", "tea", "tan", "ate", "nat", "bat"])
