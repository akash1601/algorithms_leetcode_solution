def median(num1,num2):
	nums3 = num1 + num2
	nums3.sort()
	l = len(nums3)
	med = l//2
	if (l % 2 == 0):
		 print((nums3[med-1] + nums3[med])/2)
	else:
		print(nums3[med])
        

num1 = [1,2,3]
num2 = [2]
median(num1,num2)