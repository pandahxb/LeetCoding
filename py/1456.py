class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowels = 0
        vowels = set('aeiou')
        for i in range(k):
            if s[i] in vowels:
                maxVowels += 1
        currentVowels = maxVowels
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                currentVowels -= 1
            if s[i - 1 + k] in vowels:
                currentVowels += 1
            maxVowels = max(maxVowels, currentVowels)
        return maxVowels

# Time: O(n), Space: O(1)
