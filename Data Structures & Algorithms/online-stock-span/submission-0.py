class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        new_streak = 1
        while self.stack and price >= self.stack[-1][0]:
            old_val, old_streak = self.stack.pop()
            new_streak += old_streak
        self.stack.append((price, new_streak))
        return new_streak



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)