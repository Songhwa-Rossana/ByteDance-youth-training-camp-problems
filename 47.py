def solution(n: int, l: int, r: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    res = 0
    for i in range(n):
        if a[i]%2 == 0 and l <= a[i] <= r:
            res += 1

    return res

if __name__ == '__main__':
    print(solution(5, 3, 8, [1, 2, 6, 8, 7]) == 2)
    print(solution(4, 10, 20, [12, 15, 18, 9]) == 2)
    print(solution(3, 1, 10, [2, 4, 6]) == 3)
