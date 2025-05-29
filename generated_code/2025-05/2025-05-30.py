class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        if n < 3:
            return n
        
        result = 0
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g
                if (dx, dy) not in slopes:
                    slopes[(dx, dy)] = 1
                slopes[(dx, dy)] += 1
            result = max(result, max(slopes.values(), default=0))
        return result
