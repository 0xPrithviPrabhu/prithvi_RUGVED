#butterfly or diamond
def print_diamond(n):
    print(f"\n--- Diamond Pattern (N={n}) ---\n")
    # Upper part of the diamond
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars with spaces in between
        print("* " * i)
    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars with spaces in between
        print("* " * i)
    print("-" * (2 * n + 5))
def print_butterfly(n):
    print(f"\n--- Butterfly Pattern (N={n}) ---\n")
    # Upper part of the butterfly
    for i in range(1, n + 1):
        # Print left wing
        print("* " * i, end="")
        # Print spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Print right wing
        print("* " * i)
    # Lower part of the butterfly
    for i in range(n, 0, -1):
        # Print left wing
        print("* " * i, end="")
        # Print spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Print right wing
        print("* " * i)
    print("-" * (4 * n + 5))
# Example usage
n = int(input("Enter the number of rows for the patterns: "))
if n <= 0:
    print("Input should be a positive integer.")
else:
    print_diamond(n)
    print_butterfly(n)
