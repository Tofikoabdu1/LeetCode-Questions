class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [0]*n
        stack = []
        for i in range(n):
            if col[i]!=0:
                continue
            stack.append(i)
            col[i] =1
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if col[nei] == col[node]:
                        return False
                    if col[nei] == 0:
                        col[nei] = -1 * col[node]
                        stack.append(nei)
        return True


