class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letter_to_must_come_after = defaultdict(set)
        all_letters = set()
        ret = []
        for i in range(len(words) - 1):
            all_letters |= set(words[i])
            broke_out = False
            for pos_in_word in range(min(len(words[i]), len(words[i+1]))):
                if words[i][pos_in_word] == words[i+1][pos_in_word]:
                    continue
                letter_to_must_come_after[words[i+1][pos_in_word]].add(words[i][pos_in_word])
                broke_out = True
                break
            if not broke_out and len(words[i]) > len(words[i+1]):
                return ""
        all_letters |= set(words[-1])
        fringe = deque(letter_to_must_come_after.keys())
        used = set(all_letters - set(letter_to_must_come_after.keys()))
        order = list(used)
        seen = Counter()
        while fringe:
            cur = fringe.pop()
            if cur in used:
                continue
            if len(letter_to_must_come_after[cur] - used) == 0:
                used.add(cur)
                order.append(cur)
                continue
            seen[cur] += 1
            if seen[cur] > 1:
                return ""
            fringe.append(cur)
            for required in letter_to_must_come_after[cur]:
                fringe.append(required)

        return "".join(order)


