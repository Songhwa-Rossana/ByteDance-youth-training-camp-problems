def solution(id, num, array):
    # Edit your code here
    game_to_players = {}
    target_games = set()

    for pid, gid in array:
        if pid == id:
            target_games.add(gid)
        if gid not in game_to_players:
            game_to_players[gid] = set()
        game_to_players[gid].add(pid)

    if not target_games:
        return []

    player_count = {}

    for game in target_games:
        for player in game_to_players[game]:
            if player != id:
                player_count[player] = player_count.get(player, 0) + 1

    teammates = [pid for pid, count in player_count.items() if count >= 2]

    return sorted(teammates)

if __name__ == "__main__":
    # Add your test cases here

    print(
        solution(
            1,
            10,
            [
                [1, 1],
                [1, 2],
                [1, 3],
                [2, 1],
                [2, 4],
                [3, 2],
                [4, 1],
                [4, 2],
                [5, 2],
                [5, 3],
            ],
        )
        == [4, 5]
    )
