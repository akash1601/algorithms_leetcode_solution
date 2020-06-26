def palindrome(num):
	if num < 0 or (num > 0 and num % 10 == 0):
		return False

	print(num == reverse(num))

def reverse(num):
	result = 0
	while num != 0:
		digit = num % 10
		result = result*10 + digit 
		num = int(num/10)

	return result

palindrome(121)

  # def isPalindrome(self, x: 'int') -> 'bool':
  #       return str(x) == str(x)[::-1]