def combinationSum(candidates, target):
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                continue
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    
    result = []
    candidates.sort()
    backtrack(0, [], target)
    return result

# 测试用例
candidates = [2, 3, 6, 7
