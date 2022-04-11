import numpy as np
# numpy 연산

# loop는 느리다.
# array의 모든 원소에 5를 더해서 만드는 함수

def add_5(value):
  # 빈 배열을 받을 건데 길이는 받은 value의 길이 만큼
  result = np.empty(len(value))
  for i in range(len(value)):
    result = value[i] + 5
  return result

# 1부터 10까지의 사이즈가 5인 랜덤 배열을 만들자
value = np.random.randint(1, 10, size=5)
print(value)
print(add_5(value))


# array가 커진다면 => 느림

# numpy의 기본 연산 개빠름...

x = np.arange(4)
print(x)
print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)

# 행렬간 연산
# 다차원 행렬에서도 적용 가능하다.

x = np.arange(4).reshape((2, 2))
print(x)
y = np.random.randint(10, size=(2, 2))
print(y)

print(x + y)
print(x - y)