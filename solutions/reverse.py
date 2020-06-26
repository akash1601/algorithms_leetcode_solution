def reverse(num):
	if num < 0:
		rev = -int(str(-num)[::-1])
		print(rev)
	else:
		rev = int(str(num)[::-1])
		print(rev)
	if (rev > 2**31-1) or (rev < -2**31):
		return 0


num = -123
reverse(num)