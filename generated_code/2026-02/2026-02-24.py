def generateParenthesis(n):
    def backtrack(current, left, right):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if left < n:
            backtrack(current + '(', left + 1, right)
        
        if right < left:
            backtrack(current + ')', left, right + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

#
