A = [6, 3, 8, 10, 7, 5, 2, 9, 14]

# Description
"""
Find pair where sum is equal to K
Array is unsorted. 
"""

# Brute Force Method
# k = 10


def find_pair_brute_force(arr):
    arr_len = len(arr)-1
    i = 0
    while i < arr_len:
        j = i + 1
        while j < arr_len:
            if arr[j] + arr[i] == 10:
                print(f"({arr[i]}, {arr[j]})")
            j += 1
        i += 1

find_pair_brute_force(A)

# Time Complexity:
"""
O(n^2) -> Quadratic
"""

###################################################

# Optimal way using Hash Table

# Algorithm/ Intuition:
"""
1. Find the Max in Arr
2. Create Hash (h) size = Max+1
3. Traverse Arr and check if h[k-Arr[i]] != 0, if yes print Arr[i] and k-arr[i]
"""

def find_max(arr):
    max_val = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def find_pair_using_hash(arr, k):
    max_val = find_max(arr)
    h = [0] * (max_val+1)
    for i in range(len(arr)):
        if h[k - arr[i]] != 0:
            print(f"{arr[i]} + {k-arr[i]} = {k}")
        h[arr[i]] += 1


find_pair_using_hash(A, 10)