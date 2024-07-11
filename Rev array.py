# Write a function Rev_Print that Reverse iterates and prints all the non-dummy values of an array.
# Function Call:
# arr= np.array([1 3 2 5 0 0])
# print(Rev_Print(arr, 4)) #Array, size
# Output:
# 5 2 3 1

import numpy as np

def Rev_Print(arr):
    c = 0
    for i in arr:
        if i != 0:
            c += 1

    arr2 = np.array([0] * c)
    i = 0

    while i<=len(arr2)-1:
        arr2[i]=arr[len(arr2)-1-i]
        i+=1
    return arr2

arr= np.array([1,2,3,4,5,6,7])
print(Rev_Print(arr))