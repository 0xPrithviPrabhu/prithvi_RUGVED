#Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest
def first_repeating_element(arr):
    element_index = {}
    first_repeating = -1
    min_index = len(arr)

    for i in range(len(arr)):
        if arr[i] in element_index:
            if element_index[arr[i]] < min_index:
                min_index = element_index[arr[i]]
                first_repeating = arr[i]
        else:
            element_index[arr[i]] = i

    return first_repeating
# Example usage
input_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
result = first_repeating_element(input_array)
if result != -1:
    print(f"The first repeating element is: {result}")
else:
    print("No repeating elements found.")
