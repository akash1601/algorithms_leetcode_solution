def moveZ(nums):
	zero = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[i], nums[zero] = nums[zero], nums[i]
			zero += 1

	print(nums)


moveZ([1,3,4,0,1,2,4,0,1])