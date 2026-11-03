# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
'''

i
j
5    2    9

'''

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ret = []
        for i in range(len(pairs)):
            j = i - 1
            to_insert = pairs[i]
            while j >= 0 and to_insert.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j+1] = to_insert
            ret.append(pairs.copy())
        return ret

