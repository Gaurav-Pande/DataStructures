# link:https://leetcode.com/problems/sort-characters-by-frequency/submissions/


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse = True)
        dic = collections.OrderedDict(sorted_counter)
        result=""
        for k,v in dic.items():
            result = result +v*k
        return result