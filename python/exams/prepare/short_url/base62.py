# const bi = (number) => {
#     let quotient = number;
# let reminder = [];
#
# while (quotient >= 2){
# reminder.push(quotient % 2);
# quotient = Math.floor(quotient / 2);
# }
# quotient = quotient + '';
#
# while (reminder.length > 0) {
# quotient = quotient + reminder.pop();
# }
#
# return quotient;
# }


def bi(num, n):
    quotient = num
    reminder = list()
    # codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'] # 16
    codes = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z',
    ]  # 62
    base = len(codes)

    while quotient > 0:
        reminder.append(codes[quotient % base])
        quotient = quotient // base

    return "".join(reminder[::-1])

    # while quotient >= n:
    #     reminder.appRend(quotient % n)
    #     quotient = quotient // n
    #
    # quotient = codes[quotient]
    #
    # while len(reminder) > 0:
    #     quotient = quotient + codes[reminder.pop()]
    #
    # return quotient




result = bi(10, 62)
print(result)
