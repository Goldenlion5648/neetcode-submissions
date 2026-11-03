class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        best = len(strs[0])
        for word_pos in range(1, len(strs)):
            same = 0
            for letter_pos in range(min(len(strs[0]), len(strs[word_pos]))):
                if strs[word_pos][letter_pos] == strs[0][letter_pos]:
                    same += 1
                else:
                    break
            best = min(best, same)
        return strs[0][:best]
                
