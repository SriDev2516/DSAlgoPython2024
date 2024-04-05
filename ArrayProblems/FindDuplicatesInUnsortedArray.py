A = [8, 3, 6, 4, 6, 5, 6, 8, 2, 7]

# Description:
"""
1. Array is unsorted and some numbers appear more than once
"""

# Algorithm/Intuition:
"""
1. Find the Max in the array
2. Take an Array H of size Max+1 and assign all values = 0
3. Assign H[A[i]]++
4. Traverse through H and print the elements which are greater than 0. 
"""


def find_max_in_unsorted_array(arr):
    m = 0
    for i in range(len(arr)):
        if arr[i] > m:
            m = arr[i]
    return m


def find_duplicates_in_unsorted_array(arr):
    maximum = find_max_in_unsorted_array(arr)
    h = [0] * (maximum+1)
    for i in range(len(arr)):
        h[arr[i]] += 1
    for i in range(len(h)):
        if h[i] > 1:
            print(f"{i} appears {h[i]} times")


find_duplicates_in_unsorted_array(A)