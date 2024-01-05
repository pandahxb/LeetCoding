class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*':
                res.pop()
            else:
                res.append(i)
        return ''.join(res)

# Time: O(n), Space: O(n)
