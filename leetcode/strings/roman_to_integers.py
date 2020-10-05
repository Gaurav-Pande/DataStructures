# link:  https://leetcode.com/problems/roman-to-integer/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        replace = {
            "IV": 4,
        "XL": 40,
        "CD": 400,
        "IX": 9,
        "XC": 90,
        "CM": 900
        }
        res, i = 0,0
        while i< len(s):
            try:
                if s[i] + s[i+1]  in replace:
                    res = res + replace[s[i] + s[i+1]]
                    i=i+2
                    continue
            except IndexError:
                pass
            res = res + dic[s[i]]
            i+=1
        return res
        
