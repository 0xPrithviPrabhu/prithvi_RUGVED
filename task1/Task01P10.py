#a python function to check if a given credit card number is valid or not using Luhn’s Algorithm
def luhn_check(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if the card number consists only of digits
    if not card_number.isdigit():
        return False
    
    total_sum = 0
    num_digits = len(card_number)
    parity = num_digits % 2
    
    for i, digit in enumerate(card_number):
        n = int(digit)
        # Double every second digit from the right
        if i % 2 == parity:
            n *= 2
            if n > 9:
                n -= 9
        total_sum += n
    
    # A valid card number will have a total sum that is a multiple of 10
    return total_sum % 10 == 0
# Example usage
card_number = input("Enter a credit card number to validate: ")
if luhn_check(card_number):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")
