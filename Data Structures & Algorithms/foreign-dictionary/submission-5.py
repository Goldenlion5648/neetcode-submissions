'''


'''

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letter_to_before_count = defaultdict(int)
        before_to_after = defaultdict(set)
        all_letters = set()
        for word in words:
            all_letters |= set(word)
        for cur_word_index in range(len(words)-1):
            cur_word = words[cur_word_index]
            next_word = words[cur_word_index + 1]
            for i in range(len(cur_word)):
                if i >= len(next_word):
                    if i > 0:
                        print("top")
                        return ""
                if cur_word[i] == next_word[i]:
                    continue
                if next_word[i] not in before_to_after[cur_word[i]]:
                    before_to_after[cur_word[i]].add(next_word[i])
                    letter_to_before_count[next_word[i]] += 1
                break
        fringe = [letter for letter in all_letters if not letter_to_before_count[letter]]
        # print(fringe)
        # print(before_to_after)
        answer = []
        while fringe:
            cur = fringe.pop()
            answer.append(cur)
            for after in before_to_after[cur]:
                # print(after)
                letter_to_before_count[after] -= 1
                # print(letter_to_before_count)
                if letter_to_before_count[after] == 0:
                    fringe.append(after)
        # print(answer, all_letters)
        if len(answer) != len(all_letters):
            return ""
        return "".join(answer)









            
