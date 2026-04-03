class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors= [0]*len(graph)
        safe = []
        def dfs(node):
            colors[node]=1
            for child in graph[node]:
                if colors[child] == 1:
                    return False
                if colors[child]==2:
                    continue
                if not dfs(child):
                    return False
            colors[node]=2
            safe.append(node)
            return True
        for i in range(len(graph)):
            if colors[i]==0:
                dfs(i)
        # dfs(0)
        safe.sort()
        return safe


        