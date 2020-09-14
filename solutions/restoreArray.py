from collections import defaultdict

def restoreArray(pairs):

    res = []
    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        res.append(node)
        for neighb in graph[node]:
            dfs(neighb)

    graph = defaultdict(list)
    start_or_end = set()
    for m, n in pairs:
        if m in start_or_end:
            start_or_end.remove(m)
        else:
            start_or_end.add(m)

        if n in start_or_end:
            start_or_end.remove(n)
        else:
            start_or_end.add(n)

        graph[m].append(n)
        graph[n].append(m)

    dfs(start_or_end.pop())
    return res
restoreArray([[3,5],[1,4],[2,4],[5,1]])