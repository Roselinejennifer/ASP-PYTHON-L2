def find_multiples(number, start, end):

    multiples = []
    for i in range(start, end + 1):
        if i % number == 0:
            multiples.append(i)
    return multiples



number = 5
start = 1
end = 50

multiples_of_number = find_multiples(number, start, end)
print(f"Multiples of {number} between {start} and {end} are: {multiples_of_number}")
