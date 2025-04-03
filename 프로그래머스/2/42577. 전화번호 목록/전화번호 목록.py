def solution(phone_book):
    s_phone_book = set(sorted(phone_book, key = len, reverse = True))
    l = len(s_phone_book)
    
    for num in s_phone_book:
        for j in range(len(num)):
            if num[: j] in s_phone_book:
                return False
    
    return True