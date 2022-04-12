import pandas as pd
# pandas

# 구조화된 데이터를 효과적으로 처리하고 저장할 수 있는 라이브러리
# Array 계산에 특화된 numpy를 기반으로 만들어 져서 다양한 기능 제공

# Series : numpy array가 보강된 형태 Data와 Index를 가지고 있다.

data = pd.Series([1, 2, 3, 4,])
print(data)

# 인덱스를 가지고 있고 인덱스로 접근 가능하다.
data = pd.Series([1, 2, 3, 4,], index=['a', 'b', 'c', 'd'])
print(data['a'])

# 딕셔너리로 만들 수 있다.

population_dict = {
  'korea' : 5180,
  'japan' : 12718,
  'china' : 141500,
  'usa' : 32676
}

population = pd.Series(population_dict)

print(population_dict)
# key는 인덱스, 값은 값으로!
print(population)
print(population.values)