class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j = 0, 0
        i_i, j_j = 0, 0
        while i < len(word1) and j < len(word2):
            # print(i, j)
            # for ith and jth index check for i_i and j_j
            while i_i < len(word1[i]) and j_j < len(word2[j]):
                if word1[i][i_i] != word2[j][j_j]:
                    return False
                i_i += 1
                j_j += 1

            if i_i == len(word1[i]):
                i_i = 0
                i += 1
            
            if j_j == len(word2[j]):
                j_j = 0
                j += 1

        # print(i, i_i, j, j_j)
        if i < len(word1) or j < len(word2):        # if last word is not reached
            return False

        if i_i != 0 or j_j != 0:            # should be reset to 0
            return False

        return True