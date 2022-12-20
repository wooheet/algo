DEFAULT_ALPHABET = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
DEFAULT_BLOCK_SIZE = 24
MIN_LENGTH = 5


class UrlEncoder(object):

    def __init__(self, alphabet=DEFAULT_ALPHABET, block_size=DEFAULT_BLOCK_SIZE):
        if len(set(alphabet)) < 2:
            raise AttributeError('Alphabet has to contain at least 2 characters.')
        self.alphabet = alphabet
        self.block_size = block_size
        self.mask = (1 << block_size) - 1  # 1 * 2^24 - 1
        self.mapping = range(block_size)

    def encode_url(self, n, min_length=MIN_LENGTH):
        return self.enbase(self.encode(n), min_length)

    def decode_url(self, n):
        return self.decode(self.debase(n))

    def encode(self, n):
        return (n & ~self.mask) | self._encode(n & self.mask)

    def _encode(self, n):
        result = 0
        for i, b in enumerate(reversed(self.mapping)):
            if n & (1 << i):
                result |= (1 << b)
        return result

    def decode(self, n):
        return (n & ~self.mask) | self._decode(n & self.mask)

    def _decode(self, n):
        result = 0
        for i, b in enumerate(reversed(self.mapping)):
            if n & (1 << b):
                result |= (1 << i)
        return result

    def enbase(self, x, min_length=MIN_LENGTH):
        result = self._enbase(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)

    def _enbase(self, x):
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[x]
        return self._enbase(int(x // n)) + self.alphabet[int(x % n)]

    def debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result

DEFAULT_ENCODER = UrlEncoder()


def encode(n):
    return DEFAULT_ENCODER.encode(n)


def decode(n):
    return DEFAULT_ENCODER.decode(n)


def enbase(n, min_length=MIN_LENGTH):
    return DEFAULT_ENCODER.enbase(n, min_length)


def debase(n):
    return DEFAULT_ENCODER.debase(n)


def encode_url(n, min_length=MIN_LENGTH):
    return DEFAULT_ENCODER.encode_url(n, min_length)


def decode_url(n):
    return DEFAULT_ENCODER.decode_url(n)


print(encode_url(12))

# print(31 & (1 << 31))
# print(2**31)
# print(31 & 2**31)

# print(decode_url("jy7yj"))
#
# print(DEFAULT_ENCODER.mask)
# print(~DEFAULT_ENCODER.mask)
# print((12 & ~DEFAULT_ENCODER.mask))
#
# print(DEFAULT_ENCODER.mapping)


# class DB:
#     def __init__(self, index):
#         self.index = index
#         self.url = None
#         self.short_url = ""
#
#     def insert(self, url):
#         self.url = url
#         self.index += 1
#         return self.index
#
#     def update(self, index, short_url):
#         self.index = index
#         self.short_url = short_url
#
#
# def base62(index):
#     result = ""
#     words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
#              ]
#
#     while index % 62 > 0 or result == "":
#         result = result + words[index % 62]
#         index = int(index / 62)
#
#     return result
#
#
# def generate(url):
#     db = DB(0)
#     index = db.insert(url)
#     short_url = base62(index)
#
#     print("short_url", short_url)
#
#     db.update(index, short_url)
#
#     return short_url
#
#
# generate("www.coupang.com")