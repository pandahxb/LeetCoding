from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        zero_index = -1
        for i in range(len(nums)):  # O(n)
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1
                zero_index = i
                if zero_count > 1:
                    return [0] * len(nums)
        if zero_count == 1:
            return [0 if i != zero_index else product for i in range(len(nums))]  # O(n)
        return [product // nums[i] for i in range(len(nums))]  # O(n)

# Time: O(n), Space: O(1)
