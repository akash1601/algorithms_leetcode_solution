def threeSumCloset(nums,target):
#3sumCloset
	nums.sort()
	result = nums[0] + nums[1] + nums[2]
	for i in range(len(nums)-2):
		j, k = i+1, len(nums) -1
		sum = nums[i] + nums[j] + nums[k]
		while j < k:
			if sum == target:
				return sum

			if abs(sum - target) < abs(result - target):
				result = sum

			if sum < target:
				j += 1

			elif sum > target:
				k -= 1

	print(result)

threeSumCloset([-1,2,0,5,6,1,-4],8)


