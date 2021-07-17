def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            continue
        else:
            for j in range(i-1, -1, -1):
                flag = True
                if arr[j] < arr[i]:
                    temp = arr.pop(i)
                    arr.insert(j+1, temp)
                    flag = False
                    break
            if flag:
                temp = arr.pop(i)
                arr.insert(0, temp)
    return arr


print(insertion_sort([10, 2, 3, 15, -1, 0]))
