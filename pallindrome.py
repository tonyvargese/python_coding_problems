def pall(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    return rev==num

num=int(input('enter the digit: '))
if pall(num):
    print('pallindrome')
else:
    print('not pallindrome')
    