#https://leetcode.com/discuss/general-discussion/886274/online-assessment-questions-matrix-summation

def print_matrix(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, 0, -1):
            mat[i][j] -= mat[i][j - 1]

    for i in range(m - 1, 0, -1):
        for j in range(n - 1, -1, -1):
            mat[i][j] -= mat[i - 1][j]

    return mat


def findBeforeMatrix(after):
    before = []
    linhas = len(after)
    colunas = len(after[0])
    linhas = len(after)
    colunas = len(after[0])
    bij = 0
    for i in range(linhas):

        before.append([])
        for j in range(colunas):

            if i == 0 and j == 0:
                bij = after[0][0]
            elif i == 0:
                bij = after[0][j] - after[0][j - 1]
            elif j == 0:
                bij = after[i][0] - after[i - 1][0]
            else:
                bij = after[i][j] + after[i - 1][j - 1] - after[i][j - 1] - after[i - 1][j]
            before[i].append(bij)

    return before

if __name__ == '__main__':

    print_matrix()