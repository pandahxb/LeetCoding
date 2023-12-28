class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        length = len(s)
        for char in t:
            if s[i] == char:
                i += 1
                if i == length:
                    return True
        return False

# Time: O(n), Space: O(1)
