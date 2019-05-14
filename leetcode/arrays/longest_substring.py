# Author: Gaurav Pande
#[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = 1
        string = ""
        i = 0
        result = 0
        while i < len(s):
            j = i
            while j < j + window + 1 and j < len(s):
                if s[j] in string:
                    window = 1
                    string = ""
                    i = i + 1
                    j = i
                else:
                    string = string + s[j]
                    window = window + 1
                    result = max(result,len(string))
                    j = j + 1
                    
        return result

# sliding window
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        dic = collections.defaultdict(int)
        left, right = 0, 0
        result = 0
        counter = 0
        while right < len(s):
            dic[s[right]] += 1
            if dic[s[right]] > 1:
                counter += 1
            right += 1

            while counter > 0:
                if s[left] in dic:
                    if dic[s[left]] > 1:
                        counter -= 1
                    dic[s[left]] -= 1
                left += 1
            result = max(result, right - left)
        return result

# storing the index in the dictionary
class Solution3:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength



