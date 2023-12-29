from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = current = 0
        for i in range(len(gain)):
            current += gain[i]
            highest = max(highest, current)
        return highest

# Time: O(n), Space: O(1)
