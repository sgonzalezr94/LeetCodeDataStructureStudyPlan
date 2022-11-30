from typing import List
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = 0
        max_sum = -inf
        for number in nums:
            current_subarray += number
            if max_sum < current_subarray:
                max_sum = current_subarray
            if current_subarray < 0:
                current_subarray = 0
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

response = 6

solution = Solution()
assert solution.maxSubArray(nums) == response

# Runtime: 637 ms, faster than 99.96% of Python3 online submissions for Maximum Subarray.
