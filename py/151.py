class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))  # O(n)

    # Time: O(n); Space: O(n)
