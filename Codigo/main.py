import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

p1 = 9967379
p2 = 10251250 
p3 = 10895586
t1 = 1990
t2 = 2000
t3 = 2010

iteraciones = 200

#intervalo
intervalo_inicio = -0.08
intervalo_final = -0.07

alpha = (p2*p3 - p1*p2)/(p2*p1 - p1*p3)
beta =(p1*p3 - p2*p3) /(p2*p1 - p1*p3)

def f(k):
	return 1 + alpha*sy.exp(-k*(t2-t1)) + beta*sy.exp(-k*(t3-t1))
	

def biseccion(f,a,b,n):
	xRaiz = 0
	for k in range(n):
		x = (b+a) / 2
		if f(x) * f(b) < 0:
			a = x
		elif f(x) * f(a) < 0:
			b = x
		else: 
			break
		xRaiz = x
		print("iteracion: ", k, " raiz: ", xRaiz)
	return xRaiz

k_calculado = biseccion(f,intervalo_inicio, intervalo_final,iteraciones)
print("\nK calculado: ", k_calculado)

c_calculado = (p3-p1) / (p1*sy.exp(-k_calculado*t1) - p3*sy.exp(-k_calculado*t3))
print("C calculado: ", c_calculado)

pl_calculado = p1 * ( 1 + (c_calculado*np.exp(-k_calculado * t1) ))
print("Pl calculado: ", pl_calculado, "\n")



k = sy.Symbol('k')
sy.plot(1 + alpha*sy.exp(-k*(t2-t1)) + beta*sy.exp(-k*(t3-t1)),(k,-0.1,0.1))
