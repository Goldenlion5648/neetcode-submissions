class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False]*3
        for a,b,c in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                found[0] = True

            if a <= target[0] and b == target[1] and c <= target[2]:
                found[1] = True

            if a <= target[0] and b <= target[1] and c == target[2]:
                found[2] = True
        return all(found)

