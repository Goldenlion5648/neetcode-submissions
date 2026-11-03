class WordDictionary:

    def __init__(self):
        node = lambda : defaultdict(node)
        self.trie = node()
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for letter in word:
            cur = cur[letter]
        cur["#"] = True

    def search(self, word: str) -> bool:
        def dfs(cur, index):
            if index == len(word):
                return "#" in cur
            if word[index] == ".":
                for letter in cur:
                    if letter == "#":
                        continue
                    if dfs(cur[letter], index + 1):
                        return True
                return False
            if word[index] not in cur:
                return False
            return dfs(cur[word[index]], index + 1)
        return dfs(self.trie, 0)
                
