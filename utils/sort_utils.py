def shake_sort(arr, key=lambda x: x, cmp=lambda x, y: (x > y) - (x < y), reverse=False):
    lenght = len(arr)
    is_sorted = False
    start = 0
    end = lenght - 1
    while not is_sorted:
        is_sorted = True
        for i in range(start, end):
            if cmp(key(arr[i]), key(arr[i + 1])) < 0:
                (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                is_sorted = False

        if is_sorted:
            break
        is_sorted = True
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if cmp(key(arr[i]), key(arr[i + 1])) < 0:
                (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                is_sorted = False
        start = start + 1
    if reverse:
        return arr[::-1]
    else:
        return arr


def selection_sort(arr, cmp=lambda x, y: x < y, reverse=False):
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if cmp(arr[j], arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    if reverse:
        arr.reverse()
    return arr


def cmp_persons(a, b):
    if a.get_name() < b.get_name():
        return True
    if a.get_name() == b.get_name():
        return a.get_address() < b.get_address()
    return False


def sort_persons_by_name(arr):
    return selection_sort(arr, cmp=cmp_persons, reverse=False)
