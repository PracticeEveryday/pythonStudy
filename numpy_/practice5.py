import numpy as np
# 브로드 캐스팅

# Broadcasting : shape이 다른 array끼리 연산

x = np.arange(9).reshape((3, 3))
print(x + 5)

y = np.arange(3)
print(x + y)

z = np.arange(3).reshape((3, 1))
print(y + z)

# 데이터를 잡아 늘려 형태를 맞출 수 있다면 조정하여 더한다!

# 집계 함수
# 집계 : 데이터에 대한 요약 통계를 볼 수 있다.

x = np.arange(8).reshape((2, 4))

# 합계
print(np.sum(x))
# 최소값
print(np.min(x))
# 최대값
print(np.max(x))
# 평균값
print(np.mean(x))
# 표준 편차
print(np.std(x))

# 축의 합계
print(np.sum(x, axis=0))

print(np.sum(x, axis=1))

# 마스킹 연산
# True, False array를 통해서 특정 값들을 뽑아내는 방법

x = np.arange(5)

print( x < 3 )

print( x > 5 )
# True False 인덱스 안에다가 넣어주면 바뀐 값이 출력되게 됨!
print( x[x < 3])