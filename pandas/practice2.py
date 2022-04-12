import pandas as pd
# DataFrame = 여러 개의 Series가 모여서 행과 열을 이룬 데이터

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

print(country.index)
print(country.columns)

print(country['gdp'])
print(type(country['gdp']))

# 여러개 시리즈 데이터가 모여서 데이터 프레임 형태로 이룬다.
# 근데 그 시리즈 데이터의 가장 큰 부분은 넘페이가 보강된 형테이다!

# Series도 numpy array 처럼 연산자를 쓸 수 있다.

# 1인당 gdp
gdp_per_capita = country['gdp'] / country['population']

country['gdp per capita'] = gdp_per_capita

print(country)

# 저장과 불러오기
country.to_csv("./country.csv")
country.to_excel("country.xlsx")

# 읽기
country = pd.read_csv("./country.csv")
country = pd.read_excel("country.xlsx")