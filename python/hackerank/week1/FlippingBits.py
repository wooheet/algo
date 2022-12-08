def flippingBits(n):
    result = 0

    for i in range(31, -1 , -1):
        if n // (2 ** i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2 ** i * x

    return result


# n = [2147483647, 1, 0]
n = 2147483647
# n = 1
# n = 0
print(flippingBits(n))