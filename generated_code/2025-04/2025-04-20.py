# 计算一个整数的所有约数之和 (包括1和它本身)
def sum_of_divisors(n):
    divisors_sum = 1 + n if n > 1 else 1  # 1和n本身是肯定的约数
    for i in range(2, int(n ** 0.5) + 1):  # 遍历到sqrt(n)
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # 防止重复添加平方根
                divisors_sum += n // i
    return divisors_sum

# 测试
print(sum_of_divisors(28))  # 输出：56，28的所有约数为1, 2, 4, 7, 14, 28
