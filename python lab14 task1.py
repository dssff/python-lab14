import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)

y = 15 * np.sin(10 * x) * np.cos(3 * x)

plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label='Y(x) = 15*sin(10*x)*cos(3*x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x) = 15*sin(10*x)*cos(3*x)')

plt.legend()
plt.grid(True)
plt.show()
