# perform selection sort on string in function
def selection_sort_string(s):
    # Convert string to list of characters
    char_list = list(s)
    n = len(char_list)
    # Perform selection sort
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if char_list[j] < char_list[min_index]:
                min_index = j
        # Swap the found minimum element with the current element
        char_list[i], char_list[min_index] = char_list[min_index], char_list[i]
    # Convert list of characters back to string
    sorted_string = ''.join(char_list)
    return sorted_string

# Example usage
input_string = input("Enter a string to sort: ")
sorted_string = selection_sort_string(input_string)
print("Original string:", input_string)
print("Sorted string:", sorted_string)
