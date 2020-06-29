def removeD(nums):
	x = 1
	for i in range(len(nums)-1):
		if nums[i] != nums[i+1]:
			nums[x] = nums[i+1]
			x += 1

	return(x)

removeD([1,1,2,3,4,5,5,5,6])
