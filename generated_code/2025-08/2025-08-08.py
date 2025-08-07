class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted(map(int, timePoints) + [0, 24 * 60])
        min_diff = float('inf')
        for i in range(len(timePoints) + 1):
            current_diff = (times[i] - times[i - 1]) % (24 * 60)
            min_diff = min(min_diff, current_diff)
        return min_diff
