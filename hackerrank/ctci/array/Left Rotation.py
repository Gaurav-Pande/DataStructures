# Author: Gaurav Pande
# [Problem link](https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem)

def array_left_rotation(a, n, k):
    while k > 0:
        a.append(a.pop(0))
        k = k - 1
    return a
    
    
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
