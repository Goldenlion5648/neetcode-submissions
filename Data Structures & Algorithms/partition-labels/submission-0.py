class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        window = Counter()
        ret = []
        size = 0
        for letter in s:
            window[letter] += 1
            if window[letter] == counts[letter]:
                size += window.pop(letter)
                if len(window) == 0:
                    ret.append(size)
                    size = 0
        return ret
