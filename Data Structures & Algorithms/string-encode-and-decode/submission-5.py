class Solution:
    sep = "#"
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}{self.sep}{word}" for word in strs)
    def decode(self, s: str) -> List[str]:
        pos = 0
        ret = []
        while pos < len(s):
            start = pos
            while pos < len(s) and s[pos] != self.sep:
                pos += 1
            word_size = int(s[start:pos])
            pos += 1
            ret.append(s[pos:pos+word_size])
            pos += word_size
        return ret