import numpy as np
import sympy as sy


# vectorCensoBelgica = [[1990,9967379],[2000,10251250],[2010,10895586]]
# print(vectorCensoBelgica)

p3 = 9967379
p2 = 10251250 
p1 = 10895586
t3 = 1990
t2 = 2000
t1 = 2010

def f(k):
    return (((p3 * sy.exp(-(k * t3))) - (p2 * sy.exp(-(k * t2)))) * (p1 - p2)) + ((p2 - p3) * ((p1 * sy.exp(-(k * t1))) - (p2 * sy.exp(-(k * t2)))))

a = -0.08 
b = -0.07
iteraciones = 51

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
    print(k, x, f(x))

print(kRaiz)