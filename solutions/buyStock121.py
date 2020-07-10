def bestTime(nums):
	maxP = 0
	minP = float('inf')
	for num in nums:
		minP = min(minP,num)
		profit = num - minP
		maxP = max(maxP, profit)

	print(maxP)

bestTime([7,1,2,5,6,8,5])