class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = defaultdict(int)
        graph = defaultdict(list)
        for i , j in prerequisites:
            hash[i]+=1
            graph[j].append(i)
        # print(hash)
        for i in range(numCourses):
            if i not in hash:
                hash[i] = 0
        # print(hash , graph)
        q = deque()
        res = []
        for i , j in hash.items():
            if j == 0:
                q.append(i)
        # print(q)
        while q:
            curr = q.popleft()
            res.append(curr)
            for i in graph[curr]:
                hash[i]-=1
                if hash[i]==0:
                    q.append(i)
        # print(hash)
        if len(res) == numCourses:
            return True
        return False
