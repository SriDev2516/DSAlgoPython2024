A = [3, 7, 4, 9, 12, 6, 1, 11, 2, 10]

# Description
"""
1. The numbers of arr are in sequence and start with 1 - n
2. n is known
"""

# Method 2:

"""
Algorithm:

1. Take an Array H,  whose size is Max(arr)+1
2. Traverse through the A and make the H[A[i]]++
3. Traverse through H, and print all the elements != 1

"""


def findmultiplemissingmlementsinarraymethod2(arr):
    h = [0] * 13
    for i in range(len(arr)):
        h[arr[i]] += 1
    for i in range(1, len(h)):
        if h[i] != 1:
            print(i, end=", ")


findmultiplemissingmlementsinarraymethod2(A)

# Time Complexity
"""
The time complexity is O(n)
"""
