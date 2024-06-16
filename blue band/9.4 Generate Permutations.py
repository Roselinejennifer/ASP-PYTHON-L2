def permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        result = []
        for i in range(len(lst)):
            first_element = lst[i]
            remaining_elements = lst[:i] + lst[i+1:]
            for permutation in permutations(remaining_elements):
                result.append([first_element] + permutation)
        return result
print(permutations([1,2,3]))