def deriveePartielleA(a,b,x,y):
    return 2 * (a * sommeProd(x,x) + b * somme(x) - sommeProd(x,y))

def deriveePartielleB(a,b,x,y):
    return 2 * (a * somme(x) + b * len(x) - somme(y))

def gradient(a,b,x,y):
    while(deriveePartielleA(a,b,x,y)<=0.00001 and deriveePartielleB(a,b,x,y)<=0.00001):
        res1=deriveePartielleA(a,b,x,y)
        res2=deriveePartielleB(a,b,x,y)
        a = a - res1*0.0001
        b = b - res2*0.0001
    return a,b