
def count_digits(string):
    count = 0
    for char in string:
        if char >= '0' and char <= '9':
            count += 1
    return count

# Example usage:
input_string = input("Enter a string: ")
print("Number of numerical digits:", count_digits(input_string))


