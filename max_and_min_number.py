def find_max_min(numbers):
    """docstring for MaxMin"""
    minimum = None
    maximum = None
    for num in numbers:
        if maximum is None or num > maximum:
            maximum = num
        if minimum is None or num < minimum:
            minimum = num
    if maximum == minimum:
        return [len(numbers)]
    return [minimum, maximum]

print(find_max_min([3, 8, 9, 4, 5]))
