def partition(arr, start, end):  # no cache
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):  # no cache
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr


def quicksort(l):
    if len(l) <= 1:
        return l

    pivot = l[len(l) // 2]
    less = []
    more = []
    equal = []
    for e in l:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            equal.append(e)

    return quicksort(less) + equal + quicksort(more)


l = [2, 7, 6, 3, 5, 8, 1, 4]
print(quicksort(l))
print(quick_sort(l, 0, len(l)-1))
