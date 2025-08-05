class Solution:
    def find_min_cost_to_move_chips(self, positions):
        even_cost = sum(pos // 2 for pos in positions)
        odd_cost = sum((pos + 1) // 2 for pos in positions)
        return min(even_cost, odd_cost)
