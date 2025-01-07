def solution(x, y):
    # Edit your code here
    cnt = 0
    for i in range (x, y + 1):
        if len(set(str(i))) == 1:
            cnt += 1
            
    return cnt


if __name__ == "__main__":
    # Add your test cases here

    print(solution(1, 10) == 9)
    print(solution(2, 22) == 10)
