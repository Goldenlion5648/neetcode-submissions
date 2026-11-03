'''
1 2


3 4

'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        node_to_parent = [i for i in range(n)]
        
        def find_parent(x):
            if node_to_parent[x] == x:
                return x
            found = find_parent(node_to_parent[x])
            node_to_parent[x] = found
            return found

        for a, b in edges:
            par_a = find_parent(a)
            par_b = find_parent(b)
            if par_a == par_b:
                continue
            if rank[par_a] < rank[par_b]:
                par_a, par_b = par_b, par_a
            rank[par_a] += rank[par_b]
            node_to_parent[par_b] = par_a
        
        unique_parents = set()
        for i in range(n):
            unique_parents.add(find_parent(i))
        return len(unique_parents)

