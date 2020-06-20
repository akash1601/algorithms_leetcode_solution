def twoSum(n,target):
	if len(n) <= 1:
		return False
	else:
		dict={}
		for i in range(len(n)):
			if n[i] in dict:
				print([dict[n[i]],i])
			else:
				dict[target-n[i]] = i


n = [2,3,7,1,3,1]
target = 10
twoSum(n,target)