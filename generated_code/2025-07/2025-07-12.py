# 示例：使用动态规划解决“最长回文子串”的问题（体现状态转移和二维DP数组的使用）

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True  # 单个字符是回文

    for end in range(1, n):
        for begin in range(end):
            if s[begin] == s[end]:
                if end - begin <= 2:
                    dp[begin][end] = True
                else:
                    dp[begin][end] = dp[begin + 1][end - 1]
            if dp[begin][end] and (end - begin + 1) > max_len:
                start = begin
                max_len = end - begin + 1

    return s[start:start + max_len]

# 示例调用
s = "babad"
print(longest_palindrome(s))  # 输出: "bab" 或 "aba"
