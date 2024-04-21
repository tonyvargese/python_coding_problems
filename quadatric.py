def quad(a,b,c):
    disc=b**2-4*a*c

    if disc<0:
        print('roots not exist')
        return None,None
    elif disc==0:
        root=-b/(2*a)
        return root,root
    else:
        sq_root=(b**2-4*a*c)**0.5

        root1=(-b+sq_root)/(2*a)
        root2=(-b-sq_root)/(2*a)
    return root1,root2

a=float(input('enter a'))
b=float(input('enter b'))
c=float(input('enter c'))

print('the roots are ',quad(a,b,c))

