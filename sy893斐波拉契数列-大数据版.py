def matrix_pow(matrix, power, mod):
    result = [[1, 0], [0, 1]]  # 单位矩阵
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        power //= 2
    return result
def matrix_multiply(a, b, mod):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= mod
    return c
def F(n):
    mod = 10**9 + 7
    if n == 1 or n == 2:
        return 1
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(matrix, n-1, mod)
    return result_matrix[0][0]
print(F(int(input())))