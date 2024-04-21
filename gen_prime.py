def prime(num):
    if num<=1:
        return False
    elif num<=3:
        return True
    elif num%2==0 or num%3==0:
        return False
    
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

def num(limit):
    primes=[]
    for i in range(1,limit):
        if prime(i):
            primes.append(i)
    print( primes)

limit=int(input('enter the limit: '))
print(num(limit))