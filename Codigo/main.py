import numpy as np
import sympy as sy


vectorCensoBelgica = [[1990,9967379],[2000,10251250],[2010,10895586]]
# print(vectorCensoBelgica)

p1 = 9967379
p2 = 10251250 
p3 = 10895586
t1 = 1990
t2 = 2000
t3 = 2010




#def f(k):
#    return (((p3 * sy.exp(-(k * t3))) - (p2 * sy.exp(-(k * t2)))) * (p1 - p2)) + ((p2 - p3) * ((p1 * sy.exp(-(k * t1))) - (p2 * sy.exp(-(k * t2)))))

def f(k) :
	return (p1 * (1- sy.exp(-k*t2))- p2*(1-p1*sy.exp(-k*t1)))
	
#a = -0.08 
#b = -0.07

a = 0;
b = 1;

iteraciones = 50

kRaiz = 0

for k in range(iteraciones):
    x = (a + b) / 2
    if f(x) * f(b) < 0:
        a = x
    elif f(x) * f(a) < 0:
        b = x
    else:
        break
    kRaiz = x
    print(k,a,b, x, f(x))

print(kRaiz)