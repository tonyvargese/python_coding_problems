def arms(num):
    no_digits=len(num)
    armstrong=0
    for char in num:
        armstrong=armstrong+int(char)**no_digits
    return armstrong==int(num)

num=input('enter value: ')

print('the value is: ',arms(num))