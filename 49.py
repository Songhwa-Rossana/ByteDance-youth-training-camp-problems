def solution(n: int, s: list, x: list) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    str = list(zip(s, x, range(n)))
    str.sort(key = lambda p:(-p[1], p[2]))
    return [p[0] for p in str]

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])
