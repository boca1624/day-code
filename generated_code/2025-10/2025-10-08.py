class Solution:
    def find_min_cost_to_maximize_weight(self, boxes: List[int], max_weight: int) -> int:
        # 贪心算法思想：每次选择当前剩余重量下价值最大的箱子
        boxes.sort(key=lambda x: x[1] / x[0], reverse=True)  # 按价值密度排序
        total_cost = 0
        current_weight = 0
        
        for cost, weight in boxes:
            if current_weight + weight <= max_weight:
                total_cost += cost
                current_weight += weight
            else:
                break  # 当前箱子无法加入，停止
        
        return total_cost
