# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# Takeaways
# 1. for two 'or' statements, if the first one is true, then the second is not checked in python
# 2. slicing rather than adding two strings

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # strs = sorted(strs)
        # first_word = strs[0]
        # last_word = strs[-1]
        # common_prefix = ""
        # for i in range(min(len(first_word), len(last_word))):
        #     if first_word[i] == last_word[i]:
        #         common_prefix += first_word[i]
        #     else:
        #         break
        # return common_prefix

        # first_word = strs[0]
        # total_words = len(strs)
        # max_prefix_length = len(first_word)
        # common_prefix = ""
        # for i in range(max_prefix_length):
        #     char_i = first_word[i]
        #     for j in range(1, total_words):
        #         current_word_length = len(strs[j])
        #         if current_word_length <= i or char_i != strs[j][i]:            # if first one is true, we don't even check for the second one
        #             return common_prefix
        #     common_prefix += char_i
        # return common_prefix

        # slicing instead of adding two strings
        first_word = strs[0]
        total_words = len(strs)
        max_prefix_length = len(first_word)
        for i in range(max_prefix_length):
            char_i = first_word[i]
            for j in range(1, total_words):
                current_word_length = len(strs[j])
                if current_word_length <= i or char_i != strs[j][i]:            
                    return strs[j][:i]
        return strs[0]


inst = Solution()
print(inst.longestCommonPrefix(["flower","flow","flight"]))
print(inst.longestCommonPrefix(["dog","racecar","car"]))