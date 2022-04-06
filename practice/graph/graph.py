# matplotlib
# Mathematical Plot Library 수학적으로 구성하는 라이브러리

# 파이썬에서 그래프를 그릴 수 있게 하는 라이브러리
# 꺾은 선 그래프 막대 그래프 등을 모두 지원

import numpy as np
import matplotlib.pyplot as pyplot
a = [1, 2, 3, 4, 5, 6, 7]
#a = [x for x in range(0, 20)]
#b = [x*(-2) for x in range(0, 20)]
print(a)
pyplot.plot(a)
pyplot.show()