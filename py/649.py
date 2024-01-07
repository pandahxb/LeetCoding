class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        while 'R' in s and 'D' in s:
            i = 0
            length = len(s)
            while True:
                if i >= length:
                    break
                if s[i] == 'R':
                    pop = False
                    for j in range(i + 1, length):
                        if s[j] == 'D':
                            s.pop(j)
                            length -= 1
                            pop = True
                            break
                    if pop == False:
                        for j in range(i):
                            if s [j] == 'D':
                                s.pop(j)
                                length -= 1
                                pop = True
                                break
                    if pop == False:
                        return "Radiant"
                elif s[i] == 'D':
                    pop = False
                    for j in range(i + 1, length):
                        if s[j] == 'R':
                            s.pop(j)
                            length -= 1
                            pop = True
                            break
                    if pop == False:
                        for j in range(i):
                            if s [j] == 'R':
                                s.pop(j)
                                length -= 1
                                pop = True
                                break
                    if pop == False:
                        return "Dire"
                i += 1
        if 'R' in s:
            return "Radiant"
        else:
            return "Dire"

# Time: O(n), Space: O(n)
