import pandas as pd
import numpy as np
country = pd.read_csv("./country.csv")
dataframe = pd.read_csv("./data.csv")
# print(country)
print(dataframe)

# 누락된 데이터 체크

# 튜토리얼에서 보는 데이터와 달리 현실의 데이터는 누락되어 있는 형태가 많다.

# 비어있으면(nan, None) True
print(dataframe.isnull())
# 비어있으면(nan, None) False
print(dataframe.notnull())

print(dataframe.dropna())
print(dataframe['전화번호'].fillna('전화번호 없음'))

# Series 연산
# numpy array에서 사용했던 연산자들을 활용할 수 있다.

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])

print(A + B)

# 값이 없으면 0으로 채워라
print(A.add(B, fill_value=-0))

# DataFrame 연산

A = pd.DataFrame(np.random.randint(0, 10, (2, 2)), columns=list("AB"))
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=list("BAC"))

print(A + B)

print(A.add(B, fill_value=0))

data = {
  'A' : [i+5 for i in range(3)],
  'B' : [i**2 for i in range(3)]
}

df = pd.DataFrame(data)
print(df['A'].sum())

print(df.sum())
print(df.mean())