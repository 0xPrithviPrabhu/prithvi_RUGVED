#fibonaccci squence till n-values where n is user input
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
# Example usage
num = int(input("Enter a positive integer to generate Fibonacci sequence: "))
if num <= 0:
    print("Input should be a positive integer.")
else:
    result = fibonacci_sequence(num)
    print(f"Fibonacci sequence up to {num} terms: {result}")