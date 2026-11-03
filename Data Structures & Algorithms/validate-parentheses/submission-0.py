class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for letter in s:
            if letter in "({[":
                stack.append(letter)
            else:
                if not stack:
                    return False
                if close_to_open[letter] ==  stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
