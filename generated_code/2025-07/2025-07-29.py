class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isArmstrongNumber(num):
    num_str = str(num)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == num

def findArmstrongNumbersInRange(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if isArmstrongNumber(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Example usage:
# armstrong_nums = findArmstrongNumbersInRange(100, 999)
# print(armstrong_nums)
