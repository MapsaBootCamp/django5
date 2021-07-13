def bubble_sort(arr: list) -> list:
    if not isinstance(arr, list):
        raise Exception("faghat list migiram")

    arr_size = len(arr)
    for i in range(arr_size):
        for j in range(arr_size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([1, 2, -2, 9, 51, 3, 0]))
