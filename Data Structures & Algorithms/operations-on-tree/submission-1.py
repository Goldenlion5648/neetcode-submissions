class LockingTree:
    def __init__(self, parent: List[int]):
        self.locked_nums_to_user = {}
        self.parent_to_child = defaultdict(list)
        self.child_to_parent = {}
        for i, val in enumerate(parent):
            self.parent_to_child[val].append(i)
            self.child_to_parent[i] = val
        self.parent_to_child[-1].append(0)
        sys.setrecursionlimit(50000)
            
    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked_nums_to_user:
            self.locked_nums_to_user[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked_nums_to_user and self.locked_nums_to_user[num] == user:
            self.locked_nums_to_user.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        cur = num
        while cur != -1:
            if cur in self.locked_nums_to_user:
                return False
            cur = self.child_to_parent[cur]

        def dfs(cur):
            if cur in self.locked_nums_to_user:
                return True
            if cur not in self.parent_to_child:
                return False
            return any(dfs(x) for x in self.parent_to_child[cur])

        def clear_lock_dfs(cur):
            if cur in self.locked_nums_to_user:
                self.locked_nums_to_user.pop(cur)
            if cur not in self.parent_to_child:
                return
            for x in self.parent_to_child[cur]:
                clear_lock_dfs(x)

        if not dfs(num):
            return False
        clear_lock_dfs(num)
        self.lock(num, user)
        return True
        
            







