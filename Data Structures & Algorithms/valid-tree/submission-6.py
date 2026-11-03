class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_to_parent = [i for i in range(n)]
        node_to_group_size = [1 for _ in range(n)]

        def find_parent(x):
            parent = node_to_parent[x]
            if parent == x:
                return x
            found = find_parent(parent)
            node_to_parent[x] = found
            return found

        def get_size(node):
            parent = find_parent(node)
            return node_to_group_size[parent]
            
        for x, y in edges:
            parent1 = find_parent(x)
            parent2 = find_parent(y)
            if parent1 == parent2:
                return False
            size1 = get_size(x)
            size2 = get_size(y)
            if size1 >= size2:
                node_to_parent[y] = parent1
                node_to_group_size[parent1] += node_to_group_size[y]
            else:
                node_to_parent[x] = parent2
                node_to_group_size[parent2] += node_to_group_size[x]
            
        first_parent = find_parent(0)
        for node in node_to_parent:
            if find_parent(node) != first_parent:
                return False
        return True
