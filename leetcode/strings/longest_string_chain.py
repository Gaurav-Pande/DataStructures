# link: https://leetcode.com/problems/longest-string-chain/
"""
Sort the words by word's length. (also can apply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.
"""

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key = len)
        dic = {}
        result = 0
        for word in words:
            dic[word]=1
            curr_len = len(word)
            for i in range(curr_len):
                new_word = word[:i]+word[i+1:]
                if new_word in dic and dic[new_word] + 1 > dic[word]:
                    dic[word] = dic[new_word]+1
            # print(dic)
            result = max(result, dic[word])
        return result