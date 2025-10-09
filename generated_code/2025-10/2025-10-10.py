class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            total = carry
            total += 1 if a[i] == '1' else 0
            total += 1 if b[i] == '1' else 0
            result.append('1' if total % 2 == 1 else '0')
            carry = 0 if total < 2 else 1

        if carry != 0:
            result.append('1')

        return ''.join(reversed(result))
