def solution(n, A, B, array_a):
    for i in range(n):
        array_a[i] %=10

    array_sum = sum(array_a)%10

    if array_sum == A or array_sum == B:
        return 1
    if array_sum != (A+B) % 10:
        return 0

    f = [ [0] * 10 for _ in range(n+1)]
    f[0][0] = 1

    for i in range (1, n+1):
        for j in range(10):
            f[i][j] += f[i-1][j]
            f[i][j] += f[i-1][(j - array_a[i - 1] + 10) % 10]

    return f[n][B]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, [1, 1, 1]) == 3)
    print(solution(3, 3, 5, [1, 1, 1]) == 1)
    print(solution(2, 1, 1, [1, 1]) == 2)
