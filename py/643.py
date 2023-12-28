from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currentSum = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            currentSum += nums[i - 1 + k] - nums[i - 1]
            maxSum = max(maxSum, currentSum)
        return maxSum / k

# Time: O(n), Space: O(1)
