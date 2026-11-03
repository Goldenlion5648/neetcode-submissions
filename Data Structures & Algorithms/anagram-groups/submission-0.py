class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_words = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            key_to_words[key].append(word)
        return list(key_to_words.values())