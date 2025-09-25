#check given no. is hill number or not
def hill_number(n):
    num_str = str(n)
    length = len(num_str)
    
    if length < 3:
        return False
    
    peak_found = False
    for i in range(1, length):
        if not peak_found:
            if num_str[i] > num_str[i - 1]:
                continue
            elif num_str[i] < num_str[i - 1]:
                peak_found = True
            else:
                return False
        else:
            if num_str[i] < num_str[i - 1]:
                continue
            else:
                return False
    
    return peak_found
#main code
n = int(input("Enter a number: "))