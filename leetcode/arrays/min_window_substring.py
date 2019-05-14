# https://leetcode.com/problems/minimum-window-substring/
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for elem in t:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1

        counter = len(dic)
        result = ""
        len_window = sys.maxint
        left, right = 0, 0
        head = 0
        while right < len(s):
            if s[right] in dic:
                dic[s[right]] -= 1
                if dic[s[right]] == 0:
                    counter -= 1
            right += 1
            while counter == 0:
                if s[left] in dic:
                    dic[s[left]] += 1
                    if dic[s[left]] > 0:
                        counter += 1
                if right - left < len_window:
                    len_window = right - left
                    head = left
                left += 1

        if len_window == sys.maxint:
            return ""
        else:
            return s[head:head + len_window]



