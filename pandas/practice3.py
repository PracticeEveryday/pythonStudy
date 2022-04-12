import pandas as pd
import numpy as np

gdp_dict = {
  'korea' : 169320000,
  'japan' : 516700000,
  'china' : 1409250000,
  'usa' : 2041280000
}

gdp = pd.Series(gdp_dict)

population_dict = {
  'korea' : 5180,
  'japan' : 12718,
  'china' : 141500,
  'usa' : 32676
}

population = pd.Series(population_dict)

country = pd.DataFrame({
  'population' : population,
  'gdp' : gdp
})

print(country)

gdp_per_capita = country['gdp'] / country['population']

country['gdp per capita'] = gdp_per_capita

print(country)


# Indexing/ Slicing

# loc : 명시적인 인덱스를 참조하는 인덱스/ 슬라이싱
print('\n')
print(country.loc['china'])
print('\n')
print(country.loc['korea':'japan', :'population'])

# iloc : 파이썬 스타일 정수 인덱싱/ 슬라이싱
print('\n')
print(country.iloc[0])
print('\n')
print(country.iloc[1:3, :2])

# DataFrame 새 데이터 추가/ 수정
# 리스트로 추가하는 방법과 딕셔너리로 추가하는 방법
dataframe = pd.DataFrame(columns=['이름', '나이', '주소'])
dataframe.loc[0] = ['김철수', '28', '대전']
dataframe.loc[1] = { 
  '이름':'김영희',
  '나이':'26',
  '주소':'인천'
}
print(dataframe)
dataframe.loc[1, '이름'] = '영희'
print(dataframe)

# DataFrame 새 컬럼 추가
dataframe['전화번호'] = np.nan
dataframe.loc[0, '전화번호'] = '01012345678'

print(dataframe)
print(len(dataframe))

# 컬럼 선택하기

# 컬림 이름이 하나만 있다면 Series
# 컬럼 이름이 리스트로 들어가 있다면 DataFrame

print(dataframe['이름'])
print(dataframe[['이름', '주소', '나이']])

print("\n")
print(dataframe)

country.to_csv("./country.csv")
dataframe.to_csv('./data.csv')