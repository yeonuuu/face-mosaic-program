import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def quad_func(x):
    return x**4 - 4*x**3 + 6*x**2 + x - 4


def result_plt(result):
    plt.figure(figsize=[12, 6])
    val_x = np.linspace(-2.0, 4.0, 100)
    plt.plot(val_x, quad_func(val_x), '--')
    plt.scatter(result.x, quad_func(result.x), s=100, c='r', alpha=0.75, marker='o')
    plt.annotate("minimum", (result.x, quad_func(result.x) + 0.2), size=20)
    plt.annotate("x^4 -4x^3 + 6x^2 + x -4", (1.5, 0.5), size=20)
    plt.title('minimun value of quadratic function', fontsize = 20)
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()


x0 = 1.0
result = minimize(quad_func, x0, method='SLSQP', callback=print, options={'disp' : True})

result_plt(result)
print(result.x)
