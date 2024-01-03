from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # occ1, occ2 = {}, {}
        # for i in word1:
        #     occ1[i] = occ1.get(i, 0) + 1
        # for i in word2:
        #     occ2[i] = occ2.get(i, 0) + 1
        # if set(occ1.keys()) == set(occ2.keys()) and sorted(occ1.values()) == sorted(occ2.values()):
        #     return True
        # return False

        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

# Time: O(n), Space: O(n)
