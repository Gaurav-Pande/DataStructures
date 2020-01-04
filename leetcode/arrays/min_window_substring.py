# https://leetcode.com/problems/minimum-window-substring/
# Algo:
# take l,r = 0,0
# put all the chars of t in dic and see how many are there
# start a counter as len(dic) to track if we have covered all the chars
# now traverse the s char by char
# for each char in s if you find that char in dic, then you reduce the count of that char in dic as you have found the
# element in the window, if dic[this perticular char] == 0 then we decrease our counter as we have found all such char in the s
# which are also in the t
# once the counter ==0, that means we have  window with all the values of t inside it, now we will shrink or expand the window
# now we move left window and see if that char is in th dic
# if  yes than we will increment the count of that char in the dic by 1, we will also check that if dic[that char]>0 then
# that means we need to increment the counter as we are moving right and excluding that char from the window
# we then update the window length.

# https://leetcode.com/problems/minimum-window-substring/
import sys


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        window_len = sys.maxsize
        dic = {}
        head = 0
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        counter = len(dic)
        # print("Before algo")
        # print(s[r],dic,counter)
        # print("starting algo now")
        while r < len(s):
            if s[r] in dic:
                dic[s[r]] -= 1
                if dic[s[r]] == 0:
                    counter -= 1
            r += 1
            # if r<len(s):
            # print(s[r],dic,counter)
            # all the chars in t are found in window then we will now shrink or expand
            while counter == 0:
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        counter += 1
                # print("moving from left side")
                # print(s[l],dic,counter)
                if r - l < window_len:
                    window_len = r - l
                    head = l
                # print("window length",window_len)
                l += 1
        if window_len == sys.maxsize:
            return ""
        else:
            return s[head:head + window_len]














