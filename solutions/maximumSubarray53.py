def maxSub(nums):
	curSum = maxSum = nums[0]
	for i in nums[1:]:
		curSum = max(i, curSum+i)
		maxSum = max(maxSum, curSum)

	print(maxSum)

maxSub([1,-2,1,3,2,-1,4])