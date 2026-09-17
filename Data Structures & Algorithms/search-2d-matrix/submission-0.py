class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Colm = len(matrix), len(matrix[0])

        l, r = 0, Rows * Colm - 1

        while l <= r:
            m = (l+r) // 2
            val = matrix[m//Colm][m%Colm]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True

        return False