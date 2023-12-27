from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 0
        second = -1
        for i in range(len(nums)):
            if nums[i] < nums[first]:
                first = i
            elif second is not -1 and nums[i] > nums[second]:
                return True
            elif nums[i] > nums[first]:
                second = i
        return False
