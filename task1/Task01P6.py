#given string is a anagram or not
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Create a frequency dictionary for characters in str1
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease the count for characters found in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False
    
    return True
# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
    