def solution(n: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    result = 0
    while n>1:
        if n%2 == 0 :
            result += n//2
            n = n//2

        else:
            result += (n-1)//2
            n = (n-1)//2 + 1

    return result

if __name__ == '__main__':
    print(solution(7) == 6)
    print(solution(14) == 13)
    print(solution(1) == 0)
