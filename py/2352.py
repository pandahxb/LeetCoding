from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        count = 0
        for row in grid:
            dic[str(row)] += 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += dic[str(col)]
        return count

# Time: O(n^2), Space: O(n^2)
