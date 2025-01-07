def solution(N: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    if N == 0:
        return 1  # Placeholder return

    bit_length = N.bit_length()

    mask = (1 << bit_length) - 1

    return N ^ mask


if __name__ == '__main__':
    print(solution(N=5) == 2)
    print(solution(N=10) == 5)
    print(solution(N=0) == 1)
