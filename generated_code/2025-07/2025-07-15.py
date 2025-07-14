def find_longest_palindromic_substring(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        substr1 = expand_around_center(i, i)
        # Even length palindrome
        substr2 = expand_around_center(i, i+1)
        if len(substr1) > len(longest):
            longest = substr1
        if len(substr2) > len(longest):
            longest = substr2
    return longest

# 示例
s = "babad"
print(find_longest_palindromic_substring(s))  # 输出可能是 "bab" 或 "aba"
