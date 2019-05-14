# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic = {}
        for elem in p:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
        left, right = 0, 0
        result = []
        counter = len(dic)
        while right < len(s):
            if s[right] in dic:
                dic[s[right]] -= 1
                if dic[s[right]] == 0:
                    counter -= 1
            right += 1
            while counter == 0:
                if right - left == len(p):
                    result.append(left)
                if s[left] in dic:
                    dic[s[left]] += 1
                    if dic[s[left]] > 0:
                        counter += 1
                left += 1
        return result
