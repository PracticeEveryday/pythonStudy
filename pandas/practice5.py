import pandas as pd
import numpy as np

df = pd.DataFrame({
  'col1' : [2, 1, 9, 8, 7, 4],
  'col2' : ['A', 'A', 'B', np.nan, "d", "C"],
  'col3' : [0, 1, 9, 4, 2, 3]
})

print(df)

# 값으로 정렬하기
# 오름차순
print(df.sort_values("col1"))
# 내림차순
print(df.sort_values('col1', ascending=False))

# col2를 먼저 정렬하고 같은 값에 대해서는 col1으로 정렬해라!
print(df.sort_values(['col2', 'col1']))