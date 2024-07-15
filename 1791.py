class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        n = 0
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
            n = max(n,u,v)

        print(degree)

        middle = 0
        for i in range(n+1):
            if degree[i] > degree[middle]:
                middle = i

        return middle