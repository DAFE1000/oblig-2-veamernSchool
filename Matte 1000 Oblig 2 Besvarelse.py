import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.e**(-x/4))*np.arctan(x)

def g(x):
    return np.arctan(x)-(4/((x**2)+1))

x = 2

for i in range(10):
    gx = g(x)
    dgx = 1/(1+x**2)+(8*x)/(x**2-1)**2
    if dgx != 0:
        deltax = x - gx / dgx
        if abs(deltax - x) < 0.0001:
            x = deltax

print(x)

x = np.linspace(-5, 20, 1000)
print(np.argmax(f(x)))
plt.plot(x, f(x))
plt.show()