class Solution:
    def findComplement(self, num: int) -> int:
        # 获取 num 的二进制位数
        bit_length = num.bit_length()
        # 创建一个全是 1 的数，和 num 拥有相同的位数
        all_ones = (1 << bit_length) - 1
        # 异或操作，得到补码
        return num ^ all_ones
