A = [3, 6, 8, 8, 10, 12, 15, 15, 15, 20]

# Description
"""
The array is sorted and contains one or more duplicate numbers
"""

# Algorithm/Intuition
"""
1. take i = 0 and check a[i] == a[i+1]
2. take lastDuplicate to avoid printing duplicate numbers which are more than 2 times

"""
def printduplicatesinsortedarray(arr):
    lastDuplicate = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1] and lastDuplicate != arr[i]:
            print(arr[i], end=", ")
            lastDuplicate = arr[i]

#printduplicatesinsortedarray(A)


# Printing the Duplicates with the count

# Algorithm/Intuition
"""
1. Take i = 0 and compare a[i] == a[i+1]
2. If a[i] == a[i+1] then j = i+1
3. While a[j]==a[i] j++
4. count = j-i
5. assign i = j-1
"""
def printduplicatesinsortedwithcount(arr):
    j = 0
    i = 0
    last_index = len(arr)-1

    while i < last_index:
        if arr[i] == arr[i+1]:
            j = i+1
            while arr[j] == arr[i]:
                j += 1
            print(f"The {arr[i]} appears {j-i} times")
            i = j-1
        else:
            i += 1

printduplicatesinsortedwithcount(A)
