def solution(numbers):

    even_count = 1  # Initially, an empty sum (0) is considered even
    odd_count = 0

    for num_str in numbers:
        even_digits = 0
        odd_digits = 0
        for digit in num_str:
            digit = int(digit)
            if digit % 2 == 0:
                even_digits += 1
            else:
                odd_digits += 1

        new_even_count = (even_count * even_digits) + (odd_count * odd_digits)
        new_odd_count = (even_count * odd_digits) + (odd_count * even_digits)

        even_count = new_even_count
        odd_count = new_odd_count

    return even_count

if __name__ == "__main__":
    # 你可以添加更多测试用例
    numbers = input().strip('[]').split(',')
    numbers = [int(num) for num in numbers]
    print(solution(numbers))
