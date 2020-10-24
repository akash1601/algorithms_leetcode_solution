class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2**100 % n == 0

     def isPowerOfThree(self, n: int) -> bool:
              return n>0 and 3**19 % n == 0