def numberOfIslands(nums):
	count = 0
	for i in range(len(nums)):
		for j in range(len(nums[0])):
			if nums[i][i] == '1':
				self.dfs(nums, i, j)
				count += 1
	return count

def dfs(self, nums, i, j):
	if i < 0 or j < 0 or i >= len(nums) or j >= len(nums[0]) or nums[i][j] != '1':
		return
	nums[i][j] = '#'
	self.dfs(nums, i+1, j)
	self.dfs(nums, i-1, j)
	self.dfs(nums, i, j+1)
	self.dfs(nums, i, j-1)	
numberOfIslands([1,1,1,1,1,1],
				[1,1,1,0,0,0],
				[1,1,1,1,0,0],
				[1,1,1,1,1,1])


