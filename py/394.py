class Solution:
    def decodeString(self, s: str) -> str:
        return ''.join(Solution.decode(self, 1, s))

    def decode(self, times: int, string: str) -> str:
        ret = []
        for t in range(times):
            i = 0
            while i < len(string):
                if string[i].isdigit():
                    digits = []
                    while string[i].isdigit():
                        digits.append(string[i])
                        i += 1
                    i += 1
                    new_string = []
                    bucket = 1
                    while bucket > 0:
                        new_string.append(string[i])
                        if string[i] == '[':
                            bucket += 1
                        elif string[i] == ']':
                            bucket -= 1
                        i += 1
                    ret.extend(Solution.decode(self, int(''.join(digits)), ''.join(new_string)))
                elif string[i].isalpha():
                    ret.append(string[i])
                    i += 1
                else:
                    i += 1
        return ''.join(ret)

# Time: O(n), Space: O(n)
