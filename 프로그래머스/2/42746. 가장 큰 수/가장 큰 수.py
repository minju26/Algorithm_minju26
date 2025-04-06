from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))

    def compare(x, y):
        if x + y > y + x:
            return -1  
        elif x + y < y + x:
            return 1
        else:
            return 0

    numbers.sort(key = cmp_to_key(compare))

    if numbers[0] == '0':
        return '0'

    return ''.join(numbers)
