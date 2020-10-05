#link:  https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # bruteforce method
        count = 1
        last = -1
        while last != len(s):
            last = len(s)
            count = 1
            # print(s)
            for i in range(1,len(s)):
                # print(count)
                if s[i] == s[i-1]:
                    count+=1
                elif s[i] != s[i-1]:
                    count =1
                if count == k:
                    # print(s[i-k+1:i+1])
                    s = s[:i-k+1] + s[i+1:]
                    # count =1
                    break
        return s



# using stack
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = [['#',0]]
        for i in range(len(s)):
            if stack[-1][0] == s[i]:
                stack[-1][1]+=1
                if stack[-1][1] ==k:
                    stack.pop()
            else:
                stack.append([s[i],1])
            
        # print(stack)     
        res = ""
        for c,f in stack:
            res += c*f
                    
        return res
                
                
            
        # bruteforce method
        # count = 1
        # last = -1
        # while last != len(s):
        #     last = len(s)
        #     count = 1
        #     # print(s)
        #     for i in range(1,len(s)):
        #         # print(count)
        #         if s[i] == s[i-1]:
        #             count+=1
        #         elif s[i] != s[i-1]:
        #             count =1
        #         if count == k:
        #             # print(s[i-k+1:i+1])
        #             s = s[:i-k+1] + s[i+1:]
        #             # count =1
        #             break
        # return s
                    
                
                
                    
            
            
                    
                
                
                    
            
