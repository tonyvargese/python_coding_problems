def inverse():
    rows=int(input('enter rows'))
    cols=int(input('enter cols'))

    matrix=[]
    if rows==2 and cols==2:
        for i in range(rows):
            row=[]
            for j in range(cols):
                element=int(input('enter the element'))
                row+=[element]
            matrix+=[row]
    else:
        print('invalid matrix')
    
    a,b=matrix[0][0],matrix[0][1]
    c,d=matrix[1][0],matrix[1][1]

    det=a*d-b*c

    if det==0:
        print('invese does not exist')
    
    inverse=[[d/det,-b/det],[-c/det,a/det]]
    for char in inverse:
        print(char)

inverse()
