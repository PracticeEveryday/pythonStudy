import numpy as np
import pandas as pd

df = pd.DataFrame({
  'key' : ['A', 'B', 'C', 'A', 'B', 'C'],
  'data1' : [1, 2, 3, 1, 2, 3,],
  'data2' : np.random.randint(0, 6, 6)
})

print(df)

print(df.groupby('key'))

print(df.groupby('key').sum())
print(df.groupby(['key', 'data1']).sum())


# aggregate
# groupby를 통해서 집계를 한 번에 계산하는 방법

print(df.groupby("key").aggregate(['min', np.median, max]))
print(df.groupby('key').aggregate({'data1': 'min', 'data2':np.sum}))

# filter
# groupby를 통해서 그룹 속성을 기준으로 데이터 필터링
# true면 데이터에 담아주고 false면 데이터에 담아주지 않는다.

def filter_by_mean(x) :
  return x['data2'].mean() > 3

print(df.groupby("key").mean())
print(df.groupby("key").filter(filter_by_mean))

# apply
# groupby를 통해서 묶인 데이터에 함수 적용

print(df.groupby('key').apply(lambda x : x.max()-x.min()))

# get_group
# groupby로 묶인 데이터에서 key값으로 데이터를 가져 올 수 있다.

'''
df = pd.read_csv("./univ.csv")
df.head()
df.groupby("시도").get_group("충남")
len(df.groupby("시도").get_group("충남"))

'''