#sort string in alphabetical order and print the count of each character
def sort_string_and_count(s):
    s = ''.join(sorted(s))
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in sorted(count.keys()):
        print(f"{char}: {count[char]}")
#main code
s = input("Enter a string: ")
sort_string_and_count(s)