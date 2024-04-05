A = [8, 3, 9, 25, 6, 10, 7, 2, 12, 4]

# Description:
"""
Given an unsorted array, find the maximum in Array
"""

# Algorithm/Intuition
"""
1. Take a variable Max and set Max = A[i]
2. Traverse through the array and check if A[i+] > A[i]
3. If yes, assign Max = A[i+]
"""


def find_max_in_a_array(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(f"The maximum element is {max}")


find_max_in_a_array(A)
