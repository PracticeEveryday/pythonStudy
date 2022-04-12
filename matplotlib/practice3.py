import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(10)

ax.plot(
  x, x ** 2, "o",
  markersize=15,
  markerfacecolor = 'white',
  markeredgecolor='blue'
)

plt.show()