import numpy as np
import matplotlib.pyplot as plt

#a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#print(a + b)

#a = np.ones((2, 5))
#print(a)

#a = np.zeros((3, 3))
#print(a)

#a = np.random.random((4, 5))
#print(a)

#a = np.arange(0, 10, 2)
#print(a)

#a = np.linspace(0, 1, 10)
#print(a)

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel('ось X')
plt.ylabel('ось Y')
plt.title('график функции y = x **2')
plt.grid(True)
plt.show()
