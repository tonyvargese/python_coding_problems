def factorial(num):
    result=1

    for i in range(1,num+1):
        result*=i
    print(result)

num=int(input('enter the value: '))
factorial(num)

