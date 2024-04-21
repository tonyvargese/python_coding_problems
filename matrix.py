# def matrix_addition():
#     rows = int(input("Enter the number of rows: "))
#     cols = int(input("Enter the number of columns: "))

#     # Input for first matrix
#     print("Input for first matrix:")
#     matrix1 = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             element = float(input(f"Enter element [{i+1}][{j+1}] of first matrix: "))
#             row.append(element)
#         matrix1.append(row)

#     # Input for second matrix
#     print("\nInput for second matrix:")
#     matrix2 = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             element = float(input(f"Enter element [{i+1}][{j+1}] of second matrix: "))
#             row.append(element)
#         matrix2.append(row)

#     # Perform matrix addition
#     result_matrix = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result_matrix.append(row)

#     # Print the result
#     print("\nResultant matrix after addition:")
#     for row in result_matrix:
#         print(row)

# # Call the function to perform matrix addition
# matrix_addition()

def matrix_addition():
    rows=int(input('enter rows: '))
    cols=int(input('enter cols: '))

    print('enter the input values for matrix1: ')
    matrix1=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element=int(input(f'enter the value for [{i+1},{j+1}]: '))
            row=row+[element]
        matrix1=matrix1+[row] 
    print("enter input for matrix2")
    matrix2=[]
    for j in range(rows):
        row=[]
        for i in range(cols):
            element=int(input(f'enter the element [{i+1} {j+1}]:'))
            row=row+[element]
        matrix2=matrix2+[row]
    
    result_matrix=[]

    for i in range(rows):
        row=[]
        for j in range(cols):
            element=matrix1[i][j] * matrix2[i][j]
            row=row+[element]
        result_matrix=result_matrix+[row]
    
    for row in result_matrix:
        print(row)

matrix_addition()




        
            
