# Take a binary input form user and segregate all 1's to left side and 0's to right side.

# Ex: Input : 1010011 Output : 111100

import numpy as np


l = []
num = int(input("Enter number of elements : \n"))
for i in range(0, num):
    ele = int(input())
    l.append(ele)

sorted_ls = np.sort(l)[::-1]
print(sorted_ls)