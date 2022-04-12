import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, np.pi*4, 100)

# 한 도화지에 몇개의 그래프를 그릴건지!
fig, axes = plt.subplots(2, 1)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))

plt.show()