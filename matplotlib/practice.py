# Matplotlib

# 파이썬에서 데이터를 그래프나 차트로 시각화 할 수 있는 라이브러리

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.title("First Plot")
plt.xlabel("x")
plt.ylabel("y")

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")

