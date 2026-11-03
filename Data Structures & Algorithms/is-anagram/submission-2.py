class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        buckets = [0]*26
        for letter, letter2 in zip(s, t):
            buckets[ord(letter)-ord('a')]  += 1
            buckets[ord(letter2)-ord('a')] -= 1
        return all(val == 0 for val in buckets)
            