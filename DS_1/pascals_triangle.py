# https://leetcode.com/problems/pascals-triangle/solution/


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = list()
        for row_i in range(0, numRows):
            triangle_row = [None for _ in range(row_i + 1)]
            triangle_row[0], triangle_row[-1] = 1, 1
            for row_j in range(1, len(triangle_row) - 1):
                triangle_row[row_j] = (
                    triangle[row_i - 1][row_j - 1] + triangle[row_i - 1][row_j]
                )
            triangle.append(triangle_row)
        return triangle


sol = Solution()
sol.generate(5)
