from collections import defaultdict

def solution(n, max_sum, array):
    # Edit your code here
    card_value = {
        1 : 14,
        13 : 13,
        12 : 12,
        11 : 11,
        10 : 10,
        9 : 9,
        8 : 8,
        7 : 7,
        6 : 6,
        5 : 5,
        4 : 4,
        3 : 3,
        2 : 2
    }

    count = defaultdict(int)
    for card in array:
        adjusted_card = card if card != 1 else 14
        count[adjusted_card] += 1

    num3=0
    num2=0
    current_sum=0
    for key, value in count.items():
        if value >=3:
            for other_key, other_value in count.items():
                if other_key != key and other_value>=2 :
                    sum_value = calculate_sum(key if key!=14 else 1, other_key if other_key !=14 else 1)
                    if sum_value <= max_sum:
                        if key > num3 or (key == num3 and other_key > num2):
                            num3 = key
                            num2 = other_key
                            current_sum = sum_value

    if current_sum > 0:
        return [num3 if num3 != 14 else 1, num2 if num2 != 14 else 1]
    else:
        return [0, 0]

def calculate_sum(num1, num2):
        return num1 * 3 + num2 * 2

if __name__ == "__main__":
    # Add your test cases here

    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]) == [0, 0])
