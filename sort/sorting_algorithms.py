def buuble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
    return lst


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def selection_sort(lst):
    for i in range(len(lst)):
        index = i
        for j in range(i, len(lst)):
            if lst[index] > lst[j]:
                index = j
        if index != i:
            swap(lst, i, index)
    return lst


def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            swap(lst, j, j - 1)
            j -= 1
    return lst


def find_pivot(lst, low, high):
    pivot = (low + high) // 2
    swap(lst, pivot, high)
    i = low
    for j in range(low, high + 1):
        if lst[j] < lst[high]:
            swap(lst, i, j)
            i += 1
    swap(lst, i, high)
    return i


def do_quicksort(lst, low, high):
    if low >= high:
        return
    else:
        pivot = find_pivot(lst, low, high)
        do_quicksort(lst, low, pivot - 1)
        do_quicksort(lst, pivot + 1, high)


def quicksort(lst):
    lst = do_quicksort(lst, 0, len(lst) - 1)
    return lst


def merge(first_lst, second_lst):
    length = len(first_lst)+len(second_lst)
    new_lst = [0]*length
    i = 0
    j = 0
    k = 0
    while i < len(first_lst) and j < len(second_lst):
        if first_lst[i]>second_lst[j]:
            new_lst[k]=second_lst[j]
            k += 1
            j +=1
        else:
            new_lst[k] = first_lst[i]
            k += 1
            i +=1
    index = k
    for k in range(index, length):
        if i <= len(first_lst)-1:
            new_lst[k] = first_lst[i]
            k += 1
            i += 1
        elif j <= len(second_lst)-1:
            new_lst[k] = second_lst[j]
            k += 1
            j += 1
    return new_lst


def do_mergesort(lst, low, high):
    if low > high:
        return []
    if low == high:
        return [lst[low]]
    middle = (low + high) // 2
    first_lst = do_mergesort(lst, low, middle)
    second_lst = do_mergesort(lst, middle + 1, high)
    return merge(first_lst, second_lst)


def mergesort(lst):
    lst = do_mergesort(lst, 0, len(lst) - 1)
    return lst


if __name__ == "__main__":
    import timeit
    import random
    lst = [5, 10, 6, 9, 72, 15, 8, 0, 9, -9, -15, -6, -9]

    second_lst = random.sample(range(-100, 100), 8)
    print(timeit.timeit('mergesort(second_lst)', setup='from __main__ import mergesort, second_lst', number=100000))

    third_lst = random.sample(range(-100, 100), 32)
    print(timeit.timeit('mergesort(third_lst)', setup='from __main__ import mergesort, third_lst', number=100000))

    fourth_lst = random.sample(range(-100, 100), 64)
    print(timeit.timeit('mergesort(fourth_lst)', setup='from __main__ import mergesort, fourth_lst', number=100000))

    # lst = [5,9,12,3]
    # buuble_sort(lst)
    # selection_sort(lst)
    # insertion_sort(lst)
    # lst = mergesort(lst)
    # quicksort(lst)

    # print(lst)
