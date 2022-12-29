class URLShortener:
    DOMAIN = "short_url.com/"
    DEFAULT_BLOCK_SIZE = 24

    def __init__(self, block_size=DEFAULT_BLOCK_SIZE):
        self.short_url = {}
        self.mask = (1 << block_size)

    def shorten_url(self, origin_url):
        if origin_url in self.short_url:
            id = self.short_url[origin_url]
            shorten_url = self.encode(id)
        else:
            self.short_url[origin_url] = self.mask
            shorten_url = self.encode(self.mask)
            self.mask += 1

        return self.DOMAIN + str(shorten_url)

    def encode(self, id):
        char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(char)

        ret = []

        while id > 0:
            val = id % base
            ret.append(char[val])
            id = id // base

        return "".join(ret[::-1])


shortner = URLShortener()
print(shortner.shorten_url("google.com"))
print(shortner.shorten_url("google.com"))
print(shortner.shorten_url("naver.com"))
