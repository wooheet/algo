# def conv(n, k):
#     s = ''
#     while n:
#         s += str(n%k)
#         n //= k
#     return s[::-1]
#
# # n이 소수인지 판정
# def isprime(n):
#     if n <= 1: return False
#     i = 2
#     while i*i <= n:
#         if n%i == 0: return False
#         i += 1
#     return True
#
# def solution(n, k):
#     s = conv(n,k)
#     cnt = 0
#     for num in s.split('0'):
#         if not num: continue # 빈 문자열에 대한 예외처리
#         if isprime(int(num)): cnt += 1
#     return cnt


def solution(n, k):
    word=""
    while n:            # 숫자를 k진법으로 변환
        word = str(n%k)+word
        n=n//k

    word=word.split("0")  # 변환된 숫자를 0을 기준으로 나눈다.

    count=0
    for w in word:
        if len(w)==0:    # 만약 0또는 1이거나 빈공간이라면 continue를 통해 건너뛴다.
            continue
        if int(w)<2:
            continue
        sosu=True
        for i in range(2,int(int(w)**0.5)+1): # 소수찾기
            if int(w)%i==0:
                sosu=False
                break
        if sosu:
            count+=1

    return count

n = 437674
k = 3

# n = 110011
# k = 10

print(solution(n, k))