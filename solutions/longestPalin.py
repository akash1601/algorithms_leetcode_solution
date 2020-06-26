def palindromic(s):
	rstring = s[::-1]
	if s == rstring:
		print("True")
	else:
   		print("False")
       
def longestPalindrome(s):
	if palindromic(s):
		return s

s = "abaa"
longestPalindrome(s)