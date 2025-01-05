def solution(n: int, s: list, x: list) -> list:
    assert n == len(s) == len(x)
    start = {}
    cnt = {}
    for i in range(n):
        if s[i] not in start.keys():
            start[s[i]] = i
        cnt[s[i]] = cnt.get(s[i], 0) + x[i]
    a = sorted(cnt.keys(), key=lambda s: (-cnt[s], start[s]))
    return a


if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])
