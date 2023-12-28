class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):  # O(n)
            result.append(word1[i] + word2[i])
        if len(word1) > len(word2):
            result.append(word1[len(word2):])
        elif len(word1) < len(word2):
            result.append(word2[len(word1):])
        return ''.join(result)

# Time: O(n), Space: O(n)
