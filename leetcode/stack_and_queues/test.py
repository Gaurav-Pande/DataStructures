

class Solution(object):

    def reverse(self,s):
        i=0
        j=len(s)-1

        while i < j:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i +=1
            j-=1

        return s

    def reverseII(self,s):
        res = ""
        for i in s:
            res = i + res
        return res





if __name__ == '__main__':
    ob = Solution()
    print(ob.reverseII("hello"))

