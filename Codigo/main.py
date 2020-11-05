import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

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
	return (p2 + ((p2*(p3-p1)*sy.exp(-k*t2))/(p1*sy.exp(-k*t1) - p3*sy.exp(-k*t3))) - p1 - ((p1*(p3-p1)*sy.exp(-k*t1))/(p1*sy.exp(-k*t1)-p3*sy.exp(-k*t3))))
	
#a = -0.08 
#b = -0.07

def biseccion(f,a,b,iteraciones):
	xRaiz = 0
	for k in range(iteraciones):
		x = (a+b)/2
		f_x = f(x)
		if f_x*f(b) < 0:
			a = x
		elif f_x * f(a) < 0:
			b = x
		else:
			break
		xRaiz = x
	return xRaiz	

	
a = 0.003;
b = 0.005;
iteraciones = 200



bi_x = biseccion(f,a,b,iteraciones)
print(bi_x,f(bi_x))

"""
kRaiz = 0

for k in range(iteraciones):
    x = (a + b) / 2
    f_x = f(x)
    if f_x * f(b) < 0:
        a = x
		
    if f_x * f(a) < 0:
        b = x

    kRaiz = x
    print(k,x,f_x)
""" 
"""
x = (a + b) / 2

while( (b - a)*(b-a) > 0.00000000001 ): #pregunto hasta que sea indistinguible de 0
    x = (a + b) / 2
    iteraciones += 1	
    if f(x) * f(b) < 0:
        a = x
    elif f(x) * f(a) < 0:
        b = x
    else:
        break
    kRaiz = x
"""
	
"""
print(kRaiz,iteraciones)
plt.plot(x_,y_,)
plt.xlabel = 'F(x)'
plt.ylabel = 'x'
plt.show()
"""
