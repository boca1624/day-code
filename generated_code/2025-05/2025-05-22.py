class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # 使用埃拉托斯特尼筛法（Sieve of Eratosthenes）
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
