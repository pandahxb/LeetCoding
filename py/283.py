from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        non_zeroes = [num for num in nums if num != 0]
        non_zeroes.extend([0] * zeroes)
        nums[:] = non_zeroes

# Time: O(n), Space: O(n)
