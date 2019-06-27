# https://leetcode.com/problems/pancake-sorting/submissions/
class Solution:
    def pancakeSort(self, A):
        # find the max elem
        # do a flip to bring it to first
        # do another flip to shift the max to last
        # now follow the same approach with len = len(A) - 1
        result = []
        for i in range(0, len(A)):
            mx, mx_i = self.findMax(A, len(A) - i)
            # print(mx,mx_i)
            A = self.flip(A, mx_i)
            # print("first flip",A)
            # print(i)
            result.append(mx_i + 1)
            A = self.flip(A, len(A) - i - 1)
            result.append(len(A) - i)
            # print("second flip",A)

        return result

    def findMax(self, A, l):
        mx = -sys.maxsize - 1
        mx_i = -1
        for index in range(0, l):
            if A[index] > mx:
                mx = A[index]
                mx_i = index
        return (mx, mx_i)

    def flip(self, A, index):
        return A[index::-1] + A[index + 1:]


