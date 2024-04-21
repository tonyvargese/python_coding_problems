def pattern(n):
    for i in range(n+1,-1,-1):
        print(' '*(n-i),f'*'*(2*i+1))
        # print(str(i) *i)


n=int(input('enter: '))

pattern(n)