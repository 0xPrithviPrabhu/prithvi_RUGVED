#find fabonnaci of the given number using recursion
def fabonnaci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabonnaci(n-1) + fabonnaci(n-2)
# Example usage
num = int(input("Enter a positive integer to find its Fibonacci number: "))
result = fabonnaci(num)
print(f"The {num}th Fibonacci number is: {result}")
