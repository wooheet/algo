class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False

dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
dictionary.add("hey")
print(dictionary.head)
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("h"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))
