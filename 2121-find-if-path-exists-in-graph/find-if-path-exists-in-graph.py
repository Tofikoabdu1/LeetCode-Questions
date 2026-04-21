class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        stack = []
        visited = set()
        stack.extend(graph[source])
        # print(stack)
        while stack:
            v = stack.pop()
            if v == destination:
                return True
            if v in visited:
                continue
            visited.add(v)
            stack.extend(graph[v])
        return False

        