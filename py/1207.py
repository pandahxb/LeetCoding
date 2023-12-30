from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for i in arr:
            occ[i] = occ.get(i, 0) + 1
        if len(set(occ.values())) == len(set(arr)):
            return True
        return False

# Time: O(n), Space: O(n)
