class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Construct adjacency list
        deg = [0 for _ in range(n)]
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1

        # find leaves
        leaves = deque()
        for i in range(n):
            if deg[i] <= 1:
                leaves.append(i)

        # do level traversal, triming until 2 or fewer nodes
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves) # get number of leaves
            remaining_nodes -= leaves_count # we remove leaves
            for _ in range(leaves_count):
                leaf = leaves.popleft() # get a leaf
                for neighbor in adj[leaf]: # for nodes connected to leaf
                    deg[neighbor] -= 1 # decrement degree by 1 as we are removing the leaf its connected to
                    if deg[neighbor] == 1: # rebuild leaf list
                        leaves.append(neighbor)
        
        return list(leaves)