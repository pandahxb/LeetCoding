from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[j] = char
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
        return j
