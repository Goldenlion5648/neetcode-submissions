class PrefixTree:

    def __init__(self):
        node =  lambda : defaultdict(node)
        self.trie = defaultdict(node)
        

    def insert(self, word: str) -> None:
        cur = self.trie
        for letter in word:
            cur = cur[letter]
        cur["#"] = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return "#" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True