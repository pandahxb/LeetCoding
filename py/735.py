from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            res.append(a)
            while len(res) > 1 and res[-2] > 0 and res[-1] < 0:
                if abs(res[-2]) > abs(res[-1]):
                    res.pop()
                elif abs(res[-2]) < abs(res[-1]):
                    res.pop(-2)
                elif abs(res[-2]) == abs(res[-1]):
                    res.pop()
                    res.pop()
        return res

# Time: O(n), Space: O(n)
