# Example
blacklist = ['google.com', 'daum.com']
user_url = ['image.google.com', 'example.com']

# blacklist = ['images.google.com']
# user_url = ['books.google.com']

# blacklist = ['google.com']
# user_url = ['google.com.au']

# blacklist = ['google.com']
# user_url = ['notgoogle.com']


def solution(blacklist, user_url):

    for bl in blacklist:
        for ul in user_url:
            print(ul[-(len(bl)):])
            if ul[-(len(bl)):] == bl and ul[-(len(bl)+1)] == '.':
                return True

    return False

print(solution(blacklist, user_url))