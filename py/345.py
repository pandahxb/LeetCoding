class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        start, end = 0, len(s) - 1
        while start < end:  # O(n)
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

    # Time: O(n), Space: O(n)
