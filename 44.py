import math

def solution(x: int, y: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    d = math.sqrt(x ** 2 + y ** 2)

    if d > 10:
        return 0

    score = 11 - d
    
    return math.floor(score)

if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)
