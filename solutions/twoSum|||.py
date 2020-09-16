def twoSum(A, K):
        S = -1
        count = [0] * 1001
        for i in A:
            count[i] += 1
        lo, hi = 0, 1000
        while lo < hi:
            if lo + hi >= K or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > 0 if lo < hi else 1:
                    S = max(S, lo + hi)
                lo += 1
        return S
twoSum([34,23,1,24,75,33,54,8], 60)
            