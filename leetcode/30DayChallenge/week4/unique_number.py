# link: https://leetcode.com/problems/first-unique-number/solution/
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique_nums = OrderedDict()
        self.added_nums = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # if unique_nums is not empty, return the first key in it. 
        for num in self.unique_nums.keys():
            return num
        return -1

    def add(self, value: int) -> None:
        if value in self.added_nums:
            if value in self.unique_nums:
                del self.unique_nums[value]
        else:
            self.added_nums.add(value)
            self.unique_nums[value] = None 