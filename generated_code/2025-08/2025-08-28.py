def is_palindrome(s: str) -> bool:
    def to_chars(s):
        return [char for char in s if char.isalnum()]

    def is_palindrome_recursive(chars, left, right):
        if left >= right:
            return True
        if chars[left] != chars[right]:
            return False
        return is_palindrome_recursive(chars, left + 1, right - 1)

    chars = to_chars(s.lower())
    return is_palindrome_recursive(chars, 0, len(chars) - 1)
