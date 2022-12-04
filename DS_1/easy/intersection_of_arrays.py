# https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=study-plan&id=data-structure-i

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list()
        if len(nums1) < len(nums2):
            for number in nums1:
                if number in nums2:
                    intersection.append(number)
                    nums2.remove(number)
        else:
            for number in nums2:
                if number in nums1:
                    intersection.append(number)
                    nums1.remove(number)

        return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

sol = Solution()
sol.intersect(nums1, nums2)

# 70 ms, faster than 78.76% of Python3 online submissions for Intersection of Two Arrays II.
