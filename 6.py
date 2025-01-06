def solution(n: int, H: int, A: int, h: list, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    monsters = [(h[i], a[i], i) for i in range(n)]

    dp = [1] * n

    can = [h[i] < H and a[i] < A for i in range(n)]

    for i in range(n):
        if not can[i]:
            dp[i] = 0
            continue

        for j in range(i):
            if (can[j] and h[i] > h[j] and a[i] > a[j]):
                dp[i] = max(dp[i], dp[j] + 1)
        
    return max(dp) if max(dp) > 0 else 0

if __name__ == '__main__':
    print(solution(3, 4, 5, [1, 2, 3], [3, 2, 1]) == 1)
    print(solution(5, 10, 10, [6, 9, 12, 4, 7], [8, 9, 10, 2, 5]) == 2)
    print(solution(4, 20, 25, [10, 15, 18, 22], [12, 18, 20, 26]) == 3)
