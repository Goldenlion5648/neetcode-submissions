class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for word in strs:
            ret.append(f"{len(word)}#{word}")
        return "".join(ret)


    def decode(self, s: str) -> List[str]:
        pos = 0
        ret = []
        while pos < len(s):
            cur_num = 0
            while s[pos] != "#":
                cur_num = cur_num * 10 + int(s[pos])
                pos += 1
            pos += 1
            cur_word = []
            for _ in range(cur_num):
                cur_word.append(s[pos])
                pos += 1
            ret.append("".join(cur_word))
        return ret

            