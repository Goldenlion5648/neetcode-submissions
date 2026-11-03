class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first the row
        lo = 0
        hi = len(matrix)
        while lo < hi:
            mid = (hi + lo) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                if mid + 1 < len(matrix) and matrix[mid+1][0] <= target:
                    lo = mid + 1
                else:
                    lo = mid
                    break
            elif matrix[mid][0] > target:
                hi = mid
        row = lo
        if row >= len(matrix):
            return False
        lo = 0
        hi = len(matrix[0])
        while lo < hi:
            mid = (hi + lo) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                lo = mid + 1
            elif matrix[row][mid] > target:
                hi = mid
        if lo >= len(matrix[0]):
            return False
        return matrix[row][lo] == target
            