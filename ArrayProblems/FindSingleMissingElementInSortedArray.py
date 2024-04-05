A = [1,2, 3, 4, 5, 6, 8, 9, 10, 11, 12]

# the number starts from 1 to N
# there is only one missing element in array
# the array is sorted

def FindSingleMissingElement(arr):
    for i in range(len(A)):
        if A[i]-i != 1:
            print(f"The missing element is {i+1}")
            break


FindSingleMissingElement(A)
