def intToRoman(num):
	str = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  
	roman = ""
	for i, j in enumerate (nums):
		while num >= j:
			roman += str[i]
			num -= j
		if num == 0:
			return roman

intToRoman(100)
#intToRoman
