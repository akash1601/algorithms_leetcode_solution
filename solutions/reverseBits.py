class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        while (len(s)<32):
            s = '0' + s
        kr = int(s[::-1],2)
        return kr