def zigzag(s,numRows):
	if numRows == 0 or numRows >= len(s):
		return s
	L = [''] * numRows
	index = 0
	step = 1
	for x in s:
		L[index] += x
		if index == 0:
			step = 1
		elif index == numRows - 1:
			step = -1
		index += step

	print(''.join(L))

s = "PAYPAL"
numRows = 3
zigzag(s,numRows)