def print_pyramid(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i) , '*'*(2*i-1))
        

rows=int(input('rows: '))
print_pyramid(rows)

# print(" "*(rows-i) , f'{i}*(2*i-1))
    
