import functools
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        node = lambda : defaultdict(node)
        trie = node()
        for word in dictionary:
            cur = trie
            for letter in word:
                cur = cur[letter]
            cur["#"] = True

        @functools.cache
        def dfs(s_pos):
            if s_pos == len(s):
                return 0
            ret = 1 + dfs(s_pos + 1)
            cur = trie
            og_s_pos = s_pos
            while s_pos < len(s) and s[s_pos] in cur:
                cur = cur[s[s_pos]]
                s_pos += 1
                if "#" in cur:
                    ret = min(ret, dfs(s_pos))
    
            return ret

        return dfs(0)






            