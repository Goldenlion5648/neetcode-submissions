import string
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = deque(string.ascii_lowercase)
        digit_to_letters = defaultdict(list)
        if not digits:
            return []
        for i in range(2, 10):
            for j in range(3):
                digit_to_letters[i].append(letters.popleft())
            if i in [7, 9]:
                digit_to_letters[i].append(letters.popleft())
        ret = []
        def dfs(rem_digits, so_far):
            if not rem_digits:
                ret.append(so_far)
                return
            for letter in digit_to_letters[int(rem_digits[0])]:
                dfs(rem_digits[1:], so_far + letter)
        dfs(digits, "")
        return ret
            