# def calculator(expression):
#     operators = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#     }
#     result = 0
#     current_operator = '+'
#     current_number = 0

#     for char in expression:
#         if char.isdigit():
#             current_number = current_number * 10 + int(char)
#         elif char in operators:
#             result = operators[current_operator](result, current_number)
#             current_number = 0
#             current_operator = char

#     result = operators[current_operator](result, current_number)

#     return result

# expression = input('enter the value: ')
# print('the result= ', calculator(expression))
arr = [f"{i}*2={i*2}" for i in range(1,26)]
for i in arr:
    print(i)