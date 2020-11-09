class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n,result,'',0,0)
        return result

    def dfs(self,n,result,path,left,right):
        if not self.isValid(left,right,n):
            return
        if len(path) == n*2:
            result.append(path)
            return
        self.dfs(n,result,path+'(',left+1,right)
        self.dfs(n,result,path+')',left,right+1)
        
    def isValid(self,left,right,n):
        return left >= right and left <= n and right <= n