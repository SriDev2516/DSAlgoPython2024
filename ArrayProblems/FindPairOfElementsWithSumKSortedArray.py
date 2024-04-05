A = [1, 3, 4, 5, 6, 8, 9, 10, 12, 14]

# Description:
"""
Array is sorted. 
Find the Pair which add to K
"""

# Algorithm/Intuition
"""
1. Array is sorted, so we can use two pointer method
2. i = 0 and j = len(arr)-1
3. arr[i] + arr[j] > k => j--;
    arr[i] + arr[j] < k => i++;
    arr[i] + arr[j] == 10 => i++; j--;
    
"""

def find_pair_sorted_arr(arr, k):
    i = 0
    j = len(arr)-1

    while i < j:
        if arr[i] + arr[j] == k:
            print(f"{arr[i]} + {arr[j]} = {k}")
            i += 1
            j -= 1
        elif arr[i] + arr[j] > 10:
            j -= 1
        else:
            i += 1


find_pair_sorted_arr(A, 10)

