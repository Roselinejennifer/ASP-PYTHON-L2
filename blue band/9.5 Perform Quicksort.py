def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = quicksort([x for x in array[1:] if x < pivot])
        right = quicksort([x for x in array[1:] if x >= pivot])
        return left + [pivot] + right
print(quicksort([3, 1, 4, 2]))