def trap(nums):
	if not nums or len(nums) < 3:
		return 
	water = 0
	l = 0
	r = len(nums) - 1
	l_max = nums[l]
	r_max = nums[r]
	while l < r:
		l_max = max(l_max, nums[l])
		r_max = max(r_max, nums[r])
		if l_max <= r_max:
			water += l_max - nums[l]
			l += 1
		else:
			water += r_max - nums[r]
			r += 1
	return water

trap([0,1,0,1,1,2,3,1,2,0])