class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T F F -> 0
        # T T F -> 1
        def check(num):
            return num <= target

        row = -1
        l ,r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if not check(matrix[mid][0]):
                r = mid - 1
            else:
                if mid == len(matrix) - 1:
                    row = mid
                    break
                if mid < len(matrix) - 1 and not check(matrix[mid + 1][0]):
                    row = mid
                    break
                else:
                    l = mid + 1
        
        if row == -1:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False