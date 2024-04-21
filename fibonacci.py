def fib(n):
    sequence=[]
    def fib_helper(n):
        if n<=1:
            return 1
        else:
            return fib_helper(n-1) + fib_helper(n-2)
    for i in range(n):
        sequence.append(fib_helper(i))
    return sequence

n=int(input('enter the value: '))
print('the sequence: ',fib(n))
