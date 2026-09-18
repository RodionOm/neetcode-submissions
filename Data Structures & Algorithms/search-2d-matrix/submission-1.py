class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Colms = len(matrix), len(matrix[0])
        l,r = 0, Rows * Colms - 1

        while l <= r:
            m = (l + r) // 2
            val = matrix[m//Colms][m%Colms]

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True

        return False