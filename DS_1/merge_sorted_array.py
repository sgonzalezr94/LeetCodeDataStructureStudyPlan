# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


# Runtime: 32 ms, faster than 98.73% of Python3 online submissions for Merge Sorted Array.
