def solution(X, A):
    check = [0] * X

    check_sum = 0
    for i in range(len(A)):

        # print('i', i)
        # print('A[i]-1', A[i]-1)
        # print("check[A[i]-1]", check[A[i]-1])

        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            if check_sum == X:
                print(check_sum)
                return i
    return -1


X = 5
A = [1,3,1,4,2,3,5,4]

solution(X,A)
