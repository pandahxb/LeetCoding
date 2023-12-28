from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0
        left, right = 0, len(nums) - 1
        nums.sort()
        while nums[right] > k and right != 0:
            right -= 1
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                op += 1
                continue
            if k - nums[left] > nums[right]:
                left += 1
            else:
                right -= 1
        return op

# Time: O(nlogn), Space: O(1)
