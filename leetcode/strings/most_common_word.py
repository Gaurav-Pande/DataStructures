#link:  https://leetcode.com/problems/most-common-word/
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph =  ''.join([ " " if p in '!?,.:;"\')(_-' else p.lower() for p in paragraph])
        return collections.Counter([ q for q in paragraph.split() if q not in set(banned)]).most_common()[0][0]
        
    
        
