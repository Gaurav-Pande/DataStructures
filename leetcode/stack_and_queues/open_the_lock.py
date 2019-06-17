#  https://leetcode.com/problems/open-the-lock/

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # BFS approach
        visited = set("0000")
        start = "0000"
        import collections
        q = collections.deque()
        q.append(("0000",0))
        deadends = set(deadends)
        while q:
            s,steps = q.popleft()
            if s == target:
                return steps
            if s in deadends:
                continue
            for i in range(4):
                ch = s[i]
                str1 = s[:i] + str((int(ch)+1)%10) + s[i+1:]
                str2 = s[:i] + str((int(ch)-1)%10) + s[i+1:]
                if str1 not in visited:
                    visited.add(str1)
                    q.append((str1,steps+1))
                if str2 not in visited:
                    visited.add(str2)
                    q.append((str2,steps+1))
        return -1