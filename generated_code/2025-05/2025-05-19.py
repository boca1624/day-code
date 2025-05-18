def multiply_two_polynomials(A, B):
    # A and B are lists representing polynomials, e.g. A = [3, 2, 1] represents 3 + 2x + x^2
    result_degree = len(A) + len(B) - 2
    result = [0] * (result_degree + 1)
    
    for i in range(len(A)):
        for j in range(len(B)):
            result[i + j] += A[i] * B[j]
    
    return result

# Example usage:
A = [3, 2, 1]  # 3 + 2x + x^2
B = [1, 4]     # 1 + 4x
print(multiply_two_polynomials(A, B))  # Output: [3, 14, 9, 4]
