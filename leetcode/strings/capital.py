# Author: Gaurav Pande
# [520. Detect Capital](https://leetcode.com/problems/detect-capital/description/)

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        i = 0
        list_res = []

        while i < len(word):
            if word[i].islower():
                list_res.append(False)
            else:
                list_res.append(True)
            i = i + 1
        if (all(val == True
               for val in list_res) == True):
            return  True
        elif list_res[0] == True and all(val == False
                                         for val in list_res[1:]):
            return True
        elif all(val == False
               for val in list_res) == True:
            return True
        else:
            return False
