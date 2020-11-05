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

x_ = np.arange(0,0.025,0.00001);


y_ = []

for i in x_:
	y_.append(f(i))


	
a = 0.000000001;
b = 0.1;

iteraciones = 10

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
plt.plot(x_,y_)
plt.show()
