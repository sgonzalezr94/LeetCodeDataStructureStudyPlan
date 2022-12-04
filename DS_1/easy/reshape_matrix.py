# https://leetcode.com/problems/reshape-the-matrix/?envType=study-plan&id=data-structure-i

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        array_of_elements = list()
        for array in mat:
            for value in array:
                array_of_elements.append(value)
        if len(array_of_elements) == r * c:
            mtx: List[List[int]] = list()
            for i in range(0, len(array_of_elements), c):
                mtx.append(array_of_elements[i : i + c])
            return mtx
        else:
            return mat


mat = [[1, 2], [3, 4]]
sol = Solution()
sol.matrixReshape(mat, 1, 4)

# Runtime: 89 ms, faster than 96.01% of Python3 online submissions for Reshape the Matrix.
