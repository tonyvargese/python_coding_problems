def gcd(a,b):
    while b:
        a,b = b,a%b
    return a 
def lcm(a,b):
    return (a*b)//gcd(a,b)

def gcd_lcm(num1,num2):
    GCD=gcd(num1,num2)
    LCM=lcm(num1,num2)
    print( GCD,LCM)

num1=int(input('enter the 1st value'))
num2=int(input('enter the 2st value'))

gcd_lcm(num1,num2)
        
    