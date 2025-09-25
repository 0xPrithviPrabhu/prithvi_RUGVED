#divide a given string into equal parts containing n(user input) characters of same sequence
def divide_string(s, n):
    # Check if n is valid
    if n <= 0:
        return "Input should be a positive integer."
    
    # Divide the string into parts of size n
    parts = [s[i:i+n] for i in range(0, len(s), n)]
    
    return parts
# Example usage
input_string = input("Enter a string to divide: ")
n = int(input("Enter the number of characters per part: "))
result = divide_string(input_string, n)
print("Divided parts:", result)
