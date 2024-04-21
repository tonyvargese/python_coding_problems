# def evaluate_expression(expression):
#     # Initialize variables to store the result and current operand
#     result = 0
#     current_number = 0
#     # Initialize a variable to store the current operator
#     operator = '+'

#     # Iterate through each character in the expression
#     for char in expression:
#         # If the character is a digit, update the current operand
#         if char.isdigit():
#             current_number = current_number * 10 + int(char)
#         # If the character is an operator
#         elif char in '+-*':
#             # Perform the operation based on the current operator
#             if operator == '+':
#                 result += current_number
#             elif operator == '-':
#                 result -= current_number
#             elif operator == '*':
#                 result *= current_number
#             # Update the operator for the next operation
#             operator = char
#             # Reset the current operand for the next number
#             current_number = 0
    
#     # Perform the final operation using the last operand and operator
#     if operator == '+':
#         result += current_number
#     elif operator == '-':
#         result -= current_number
#     elif operator == '*':
#         result *= current_number

#     return result

# # Test cases
# expression = input('Enter: ')
# print('The result is:', evaluate_expression(expression))

def calculator(expression):
    curr=0
    operator="+"
    result=0

    for char in expression:
        if char.isdigit():
            curr=curr*10+int(char)
        elif char in "+-*":
            if operator=="+":
                result+=curr
            elif operator=='-':
                result-=curr
            elif operator=='*':
                result*=curr
            
            curr=0
            operator=char
    if operator=='+':
        result+=curr
    elif operator=='-':
        result-=curr

    elif operator=='*':
        result*=curr
    return result


expression =input('enter the value: ')
print('the result= ',calculator(expression))

