A = [6, 3, 8, 10, 15, 155,  2, 4, 1, 1, 1, 1, 2, 4, 5, -2, -2, -1]


def fin_max_min_single_scan(arr):
    max_val = arr[0]
    min_val = arr[0]
    for i in range(1, len(arr)-1):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
    print(f"Max: {max_val} \nMin: {min_val}")


fin_max_min_single_scan(A)