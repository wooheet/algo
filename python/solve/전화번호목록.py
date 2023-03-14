def solution(phone_book):
    answer = True

    # for i in range(len(phone_book)-1):
    #     for j in range(len(phone_book)):
    #         if i == j:
    #             continue
    #
    #         a = phone_book[i]
    #         if a == phone_book[j][:len(a)]:
    #             answer = False
    #             break
    #
    # return answer

    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]

solution(phone_book)