class Node:
    def __init__(self,val=None):
        self.val = val
        self.childs = []

def dfs(node,cache):
    if not node:
        return 0

    for c in node.childs:
        cache[node.val].extend(dfs(c,cache))
    cache[node.val].extend([node.val])

    return cache[node.val]

def solution(node):
    import collections
    cache = collections.defaultdict(list)
    dfs(n,cache)

    maxx = float('-inf')
    result = None
    
    for item in cache:
        if len(cache[item])>1:
            val = sum(cache[item])/len(cache[item])
        
            if val>maxx:
                result = item
                maxx = val
    return result
    

# Testcase
n = Node(20)
n12 = Node(12)
n12.childs = [Node(11), Node(2), Node(3), Node(100)]
n18 = Node(18)
n18.childs = [Node(15), Node(8)]

n.childs = [n12,n18]


solution(n)