def maxWater(heights):
	L = 0
	R = len(heights) - 1
	width = len(heights) - 1
	maxw =0
	for w in range(width,0,-1):
		if heights[L] < heights[R]:
			maxw = max(maxw,w*heights[L])
			L = L+1
		else:
			maxw =max(maxw,w*heights[R])
			R = R-1
	print(maxw)

maxWater([1,4,3,2,1,4])