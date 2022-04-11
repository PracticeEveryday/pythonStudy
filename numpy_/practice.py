import numpy as np

print(list(range(10)))

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([3, 1.4, 2, 3, 4])
print(b)

c = np.array([[1, 2], [3, 4]])
print(c)

d = np.array([[1, 2],
              [3, 4]])
print(d)

e = np.array([1, 2, 3, 4], dtype='float')
print(e)
print(e.dtype)
e.astype(int)
print(e)
print(e.dtype)


# 다양한 배열 만들기
a = np.zeros(10, dtype=int)
print(a)

# 3 * 5 행렬을 만들어서 float형으로 1 채워라
a = np.ones((3, 5), dtype=float)
print(a)

# arange(start, end, step)
# 시작값 부터 끝 값까지 step 만큼 띄어서 만들어라
a = np.arange(0, 20, 2)
print(a)

# linspace(start, and, count)
# start부터 end까지 count개로 나누어서 만들어 주세요
a = np.linspace(0, 1, 5)
print(a)

# 난수로 채워진 배열 만들기

# 인자로 튜플 (shape(2, 2)) 2 * 2 형태의 배열을 만들어 줘라 
a = np.random.random((2, 2))
print(a)

# (average, standard deviation, shape(2, 2))
# 평균이 0이고 표준편차가 1인 2 * 2 형태의 배열을 만들어 줘라
a = np.random.normal(0, 1, (2, 2))
print(a)

# (start, end, shape(2, 2))
# start 부터 end까지 랜덤 수를 2 * 2 형태의 배열로 만들어 줘라 
a = np.random.randint(0, 10, (2, 2))
print(a)