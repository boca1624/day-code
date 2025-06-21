def maxProduct(nums):
    if not nums:
        return 0
    
    # Initialize variables
    max_prod = min_prod = result = nums[0]
    
    # Traverse through the array
    for num in nums[1:]:
        # If the number is negative, swap max_prod and min_prod
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Update max_prod and min_prod for the current number
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        # Update result with the maximum product found so far
        result = max(result, max_prod)
    
    return result
