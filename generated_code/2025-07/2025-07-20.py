# LeetCode 动态规划主题示例：最长回文子串（中心扩展法 + DP 记忆表）

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    # dp[i][j] 表示 s[i:j+1] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    for j in range(n):
        for i in range(j + 1):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
    return s[start:start + max_len]

# 示例
s = "babad"
print(longest_palindrome(s))  # 输出可能是 "bab" 或 "aba"
