A = [6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]

# Description:
# the elements are in sequence and sorted
# there might be one or more missing elements

# Method 1
"""
Algorithm:

1. Find the difference between the number and its index
2. We will compare the difference through the elements
3. If the difference d != A[i]-i, then there may be one or more than one missing element
4. Write a while loop such that while diff < A[i]-i, print (diff+i) and (diff++)

"""

def findMultipleMissingElementsInAnArray(arr):
    diff = arr[0]-0
    for i in range(len(arr)):
        if arr[i]-i != diff:
            while diff < arr[i]-i:
                print(diff+i, end=", ")
                diff += 1

findMultipleMissingElementsInAnArray(A)




"""
Time Complexity: O(n)
The inner while loop can be ignored as it runs for negligible times.
"""