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

#def f(k) :
#	return (p2 + ((p2*(p3-p1)*sy.exp(-k*t2))/(p1*sy.exp(-k*t1) - p3*sy.exp(-k*t3))) - p1 - ((p1*(p3-p1)*sy.exp(-k*t1))/(p1*sy.exp(-k*t1)-p3*sy.exp(-k*t3))))
	
	
#def f(k):
#	return (p2-p1)+(p3-p2)*(p2*sy.exp(-k*t2) - p1*sy.exp(-k*t1))/(p1*sy.exp(-k*t1) - p3*sy.exp(-k*t3))
	
	
#def f(k):
#	return (p2-p1)*(p1*sy.exp(-k*t1) - p3*sy.exp(-k*t3))+(p3-p2)*(p2*sy.exp(-k*t2) - p1*sy.exp(-k*t1))

alpha = 1
beta = (p2*p3 - p1*p2)/(p2*p1 - p1*p3)
gamma =(p1*p3 - p2*p3) /(p2*p1 - p1*p3)
print('alpha',alpha,'beta',beta,'gamma',gamma)
def fun_k(k):
	return 1 + beta*sy.exp(-k*(t2-t1)) + gamma*sy.exp(-k*(t3-t1))
	
	
#a = -0.08 
#b = -0.07

def biseccion(f,a,b,n):
	xRaiz = 0
#	print(f,a,b,n)
	for k in range(n):
#		print(k)
		x = (b+a)/2
		f_x = f(x)
		f_a = f(a)
		f_b = f(b)
#		print('x',x,'f_x',f_x,'f_a',f_a,'f_b',f_b)
		if f_x*f_b<0:
			a = x
#			print('a',a)
		elif f_x*f_a<0:
			b = x
#			print('b',b)
		else: 
#			print('break')
			break
		xRaiz = x
		print(k,a,x,b)
	return xRaiz

bi_x = biseccion(fun_k,-0.1,0,200)
print(bi_x,fun_k(bi_x))

k = sy.Symbol('k')
sy.plot(1 + beta*sy.exp(-k*(t2-t1)) + gamma*sy.exp(-k*(t3-t1)),(k,-0.1,0.1))

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
	print(kRaiz,iteraciones)
"""
"""	
# 100 linearly spaced numbers
f_ = np.vectorize(f)
x = np.linspace(-10,10,10000)
y = f_(x)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y, 'r')
plt.show()
"""