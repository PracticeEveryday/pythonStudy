import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

fig, ax = plt.subplots(figsize=(12,4))

ax.bar(x, x*2)

plt.show()

x = np.random.rand(3)
z = np.random.rand(3)
y = np.random.rand(3)

data = [x, y, z]

fig, ax = plt.subplots()

x_ax = np.arange(3)

for i in x_ax:
  ax.bar(x_ax, data[i],
  bottom=np.sum(data[:i], axis=0))
ax.set_xlabel(x_ax)
ax.set_xticklabels(["A", "B", "C"])

plt.show()

fig, ax = plt.subplots()
data = np.random.rand(1000)
ax.hist(data, bins=50)

plt.show()