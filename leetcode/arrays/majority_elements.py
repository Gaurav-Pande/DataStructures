#link:https://leetcode.com/problems/majority-element-ii
"""
Explanation

Think of it this way: Find three different votes and hide them. Repeat until there aren't three different votes left. A number that originally had more than one third of the votes now still has at least one vote, because to hide all of its votes you would've had to hide more than three times one third of the votes - more votes than there were. You can easily have false positives, though, so in the end check whether the remaining up to two candidates actually had more than one third of the votes.

My code does just that: Collect (count) the votes for every number, but remove triples of three different votes on the fly, as soon as we have such a triple.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ctr = collections.Counter()
        for n in nums:
            print(ctr)
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]