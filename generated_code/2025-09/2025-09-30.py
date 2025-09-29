class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Store the original number
        original = x
        reversed_num = 0
        
        # Reverse the number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Check if the original number is equal to the reversed number
        return original == reversed_num
