class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        target = len(graph)-1
        # print(target)
        res = []
        def dfs(node , path):
            if node == target:
                res.append(path[::])
                return
            for i in graph[node]:
                path.append(i)
                dfs(i , path)
                path.pop()
        dfs(0 , [0])
        return res
        

        