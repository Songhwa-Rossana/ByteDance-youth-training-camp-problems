def solution(s: str) -> str:
    # write code here
    s = s.lstrip('0')
    if s == '':
        s = '0'

    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, ''

    int_part_with_commas = ''
    for i, char in enumerate(reversed(int_part)):
        if i > 0 and i % 3 == 0:
            int_part_with_commas = ',' + int_part_with_commas

        int_part_with_commas = char + int_part_with_commas

    if dec_part:
        result = int_part_with_commas + '.' + dec_part
    else:
        result = int_part_with_commas

    return result


if __name__ == '__main__':
    s = input("s = ")
    print(solution(s))
