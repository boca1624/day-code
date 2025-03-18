from collections import defaultdict

class TwoSum:
    def __init__(self):
        """Initialize an empty hash table to store numbers and their counts."""
        self.num_counts = defaultdict(int)

    def add(self, number: int) -> None:
        """Add the number to the internal data structure."""
        self.num_counts[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the given value.
        """
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                if complement != num or self.num_counts[num] > 1:
                    return True
        return False

# 示例用法
two_sum = TwoSum()
two_sum.add(1)
two_sum.add(3)
two_sum.add(5)
print(two_sum.find(4))  # True (1 + 3)
print(two_sum.find(7))  # True (3 + 4)
print(two_sum.find(10)) # False
