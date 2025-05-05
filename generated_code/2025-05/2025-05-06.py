from typing import List

def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    LeetCode 134 - Gas Station
    贪心思路：如果总油量 < 总消耗，一定无法完成；否则从某个站点出发一定可行。
    """
    total_gas, total_cost = sum(gas), sum(cost)
    if total_gas < total_cost:
        return -1

    start_station = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start_station = i + 1
            tank = 0
    return start_station

# 示例用法
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost))  # 输出应为 3
