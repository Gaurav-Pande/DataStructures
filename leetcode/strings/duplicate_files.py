# link: https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for item in paths:
            l = item.split(" ")
            direc = l[0]
            for elem in l[1:]:
                file_name, text = elem.split("(")
                dic[direc].append((file_name, text[:-1]))
        # print(dic)                
            
        dic2 = collections.defaultdict(list)
        result = []
        for d,f in dic.items():
            for file_name, txt in f:
                dic2[txt].append(str(d)+"/" + str(file_name))
        # print(dic2)
        
        for k,v in dic2.items():
            if len(v)>1:
                result.append(v)
        
        # print(result)
        return result
        
    
        
        