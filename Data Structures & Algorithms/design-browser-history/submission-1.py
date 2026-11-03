class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pos+1]
        self.stack.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos -= steps
        self.pos = max(0, self.pos)
        return self.stack[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += steps
        self.pos = min(len(self.stack) - 1, self.pos)
        return self.stack[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)