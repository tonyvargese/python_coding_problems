def transpose():
    rows=int(input('no of rows'))
    cols=int(input('no of cols'))
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element=int(input('enter element: '))
            row.append(element)
        matrix.append(row)

    transpose=[]
    for i in range(rows):
        transpose.append([0]*cols)

    for i in range(rows):
        for j in range(cols):
            transpose[i][j]=matrix[j][i]
    print(transpose)

transpose()
