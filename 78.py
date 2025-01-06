def solution(inputArray):
    # Please write your code here
    if not inputArray:
        return 0
    
    inputArray.sort()

    merged = []
    for interval in inputArray:
        if not merged or merged[-1][1] + 1 < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    total_points = 0
    for start, end in merged:
        total_points += end - start + 1

    return total_points

if __name__ == "__main__":
    #  You can add more test cases here
    testArray1 = [[1,4], [7, 10], [3, 5]]
    testArray2 = [[1,2], [6, 10], [11, 15]]

    print(solution(testArray1) == 9 )
    print(solution(testArray2) == 12 )
