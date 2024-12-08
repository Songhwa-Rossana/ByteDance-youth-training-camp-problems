#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<int> solution(int id, int num, vector<pair<int, int>> array) {
    // 创建游戏到玩家的映射
    unordered_map<int, unordered_set<int>> game_to_players;
    unordered_set<int> target_games;

    // O(N) - 只遍历一次数组
    for (pair<int, int> pair : array) {
        int pid = pair.first;
        int gid = pair.second;

        if (pid == id) {
            target_games.insert(gid);
        }
        game_to_players[gid].insert(pid);
    }

    // 如果目标玩家没有游戏记录，直接返回
    if (target_games.empty()) {
        return {};
    }

    // 使用计数器统计与目标玩家的共同游戏次数
    unordered_map<int, int> player_count;

    // 遍历目标玩家的游戏
    for (int game : target_games) {
        for (int player : game_to_players[game]) {
            if (player != id) {
                player_count[player]++;
            }
        }
    }

    // 筛选出符合条件的玩家
    vector<int> teammates;
    for (pair<int, int> pair : player_count) {
        int pid = pair.first;
        int count = pair.second;
        if (count >= 2) {
            teammates.push_back(pid);
        }
    }

    // 排序结果
    sort(teammates.begin(), teammates.end());
    return teammates;
}

int main() {
    vector<pair<int, int>> array = {
        {1, 1}, {1, 2}, {1, 3}, {2, 1}, {2, 4}, {3, 2}, {4, 1}, {4, 2}, {5, 2}, {5, 3}
    };

    vector<int> result = solution(1, 2, array);

    vector<int> expected = {4, 5};
    cout << (result == expected ? "Pass" : "Fail") << endl;

    return 0;
}
