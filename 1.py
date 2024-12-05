def solution(cards):
    # Edit your code here
    result = 0

    for card in cards:
        result ^= card

    return result


if __name__ == "__main__":
    # Add your test cases here
    cards = input("cards = ").split()
    cards = [int(card) for card in cards]
    print(solution(cards))
