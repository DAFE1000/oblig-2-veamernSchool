import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.e**(-x/4))*np.arctan(x)

#(np.arctan(x)-(4/((x**2)+1))) = 0

x = np.linspace(-5, 20, 1000)
plt.plot(x, f(x))
plt.show()

print("It barks at no one else but me like It's seen a ghost I guess it's seen the sparks flowing no one else would know hey man slow down, slow down idiot, slow down, slow down sometimes I get overcharged that's when you see sparks they ask me where the hell I'm going at a thousand feet per second hey man slow down, slow down idiot, slow down, slow down hey man slow down, slow down idiot, slow down, slow down")