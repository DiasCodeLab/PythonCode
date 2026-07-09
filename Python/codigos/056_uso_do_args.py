

def soma(*args):

    return sum(args)

somar = soma(1,2,3,4,5,6)

print(somar)


a,b,c,*args = 1,2,3,4,5,6,7

print(a,b,c,args)