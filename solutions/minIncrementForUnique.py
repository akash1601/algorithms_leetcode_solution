def minIncrementForUnique(self, A: List[int]) -> int:
        ans=0
        if A:
            A.sort()
            pre=-1
            for a in A:
                if pre<a:
                    pre=a
                else:
                    pre+=1
                ans+=(pre-a)
        return ans