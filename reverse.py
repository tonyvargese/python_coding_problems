def reverse(num):
    num=list(num)
    t=''
    l=0
    right=len(num)-1
    while l<right:
        num[l],num[right]=num[right],num[l]
        l+=1
        right-=1
    for char in num:
        t+=char
    return t

num=input('enter the string: ')
print('reversed string: ',reverse(num))
