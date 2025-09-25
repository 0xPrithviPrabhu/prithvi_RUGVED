#Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order
def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)
    # Create a new matrix to store the rotated version
    rotated = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    
    return rotated
def print_spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result
# Example usage
n = int(input("Enter the size of the n*n matrix: "))
if n <= 0:
    print("Input should be a positive integer.")
else:
    matrix = []
    print("Enter the matrix row by row (space-separated values):")
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"Each row must have exactly {n} elements.")
            exit(1)
        matrix.append(row)
    
    rotated_matrix = rotate_matrix_90_clockwise(matrix)
    print("\nRotated Matrix by 90° Clockwise:")
    for row in rotated_matrix:
        print(" ".join(map(str, row)))
    
    spiral_order = print_spiral_order(matrix)
    print("\nSpiral Order of the original matrix:")
    print(" ".join(map(str, spiral_order)))
