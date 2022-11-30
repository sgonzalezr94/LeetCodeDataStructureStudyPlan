# https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = True
            else:
                return True
        return False
