def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            print("hellp")
            continue
        else:
            for j in range(i-1, -1, -1):
                print("bye: ", j)
                print("i: ", i)
                if arr[j] < arr[i]:
                    print("salam")
                    temp = arr.pop(i)
                    arr.insert(j, temp)
                    break
            temp = arr.pop(i)
            arr.insert(0, temp)
    return arr


# print(list(range(0, -1, -1)))

print(insertion_sort([10, 2, 3, 15, -1, 0]))
