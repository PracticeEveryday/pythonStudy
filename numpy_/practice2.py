import numpy as np

x2 = np.random.randint(0, 10, size=(3, 4))
# x3 = np.random.randint(0, 10, (3, 4))

print(x2)
# print(x3)

# 몇 차원 배열인가.
print(x2.ndim)

# 행렬의 모양은?
print(x2.shape)

# 원소가 얼마만큼 들어있는지
print(x2.size)

# 데이터 타입
print(x2.dtype)


# 찾기
x = np.arange(7)

print(x[3])

# 7번째 인덱스 없음
#print(x[7])

x[0] = 10
print(x)

# Slicing

x = np.arange(7)

# start : end-1까지 출력
print(x[1:4])
print(x[1:])
print(x[:4])
# step 2씩 건너뛴 값을 출력해주세요
print(x[::2])
