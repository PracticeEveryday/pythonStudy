import numpy as np

# 모양 바꾸기

# reshapte : array의 shape를 변경한다.

x = np.arange(8)
print(x)
print(x.shape)

# x를 reshape하는 데 튜플로 들어가고 그 모양이 2*4 배열로 만들어주세요!
x2 = x.reshape((2, 4))
print(x2)
print(x2.shape)

# 이어붙이기
# concatenate : array를 이어 붙인다.

x = np.array([0, 1, 2])
y = np.array([3, 4, 5])

print(np.concatenate([x, y]))

# np.concatenate: axis 축을 기준으로 이어 붙일 수 있다.
# 세로 방향!
matrix = np.arange(4).reshape(2, 2)
print(np.concatenate([matrix, matrix], axis=0))

# 가로 방향!
matrix = np.arange(4).reshape(2, 2)
print(np.concatenate([matrix, matrix], axis=1))

# 나누기
# np.split : axis 축 기준으로 나눌 수 있다.

# 세로 방향!
matrix = np.arange(16).reshape(4, 4)
# split(나눌 인자, 리스트(어디 인덱스로 나눌 것인지), 방향)
upper, lower = np.split(matrix, [3], axis=0)

print(upper)
print(lower)

# 가로 방향!

matrix = np.arange(16).reshape(4, 4)
# split(나눌 인자, 리스트(어디 인덱스로 나눌 것인지), 방향)
left, right = np.split(matrix, [3], axis=1)

print(left)
print(right)