# 함수로 데이터 처리하기

# apply를 통해서 함수로 데이터를 다룰 수 있다.

import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(5), columns=["Num"])

def squre(x):
  return x ** 2


print(df["Num"].apply(squre))
print(df["Num"].apply(lambda x : x ** 3))

df = pd.DataFrame(columns=["phone"])

df.loc[0] = "010-1234-1235"
df.loc[1] = "공일공-일이삼사-1235"
df.loc[2] = "010-1234-일이삼오"
df.loc[3] = "공1공-1234-1이3오"

df["preprocess_phone"] = ''

print(df)

def get_preprocess_phone(phone) :
  mapping_dict = {
    '공': '0',
    '일': '1',
    '이': '2',
    '삼': '3',
    '사': '4',
    '오': '5',
    '-': '',
    '.': '',
  }
  for key, value in mapping_dict.items():
    phone = phone.replace(key, value)
  return phone

df["preprocess_phone"] = df["phone"].apply(get_preprocess_phone)

print(df)

df = pd.DataFrame({
  "Sex" : ['Male', 'Male', "Female", "Female", "Male"]
})

print(df)

df["Sex"] = df.Sex.replace({"Male" : 0, "Female" : 1})
df.Sex.replace({"Male" : 0, "Female" : 1}, inplace=True)
print(df)