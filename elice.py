import pandas as pd
import numpy as np
import matplotlib as plt

FILE_PATH = './Korea_Income_and_Welfare.csv'

KOR_inc_wel_df = pd.read_csv(FILE_PATH)

# 처음 다섯개 불러오기
print(KOR_inc_wel_df.head())
print(KOR_inc_wel_df.shape)


def return_region_name(x):
    if x == 1:
        return 'Seoul'
    elif x==2:
        return 'Kyeong-gi'
    elif x==3:
        return 'Kyoung-nam'
    elif x==4:
        return 'Kyoung-buk'
    elif x==5:
        return 'Chung-nam'
    elif x==6:
        return 'Gang-won &. Chung-buk'
    elif x==7:
        return 'Jeolla & Jeju'


# apply method == map과 유사
KOR_inc_wel_df['region_name'] = KOR_inc_wel_df['region'].apply(return_region_name)

# .(닷)을 이용해서는 새로운 열만들기는 안 됨!!
# 덮어씌우기는 가능!
#KOR_inc_wel_df.'region_name' = 

print(KOR_inc_wel_df)

# 묶고 싶은 데이터끼리 묶어주기
print(KOR_inc_wel_df.groupby('id').count())
print(KOR_inc_wel_df.groupby('region_name')['income'].mean())
# 평균값
print(KOR_inc_wel_df.groupby('region_name')['income'].mean().sort_values())

print(KOR_inc_wel_df.groupby('education_level')['income'].mean().sort_values())
edu_income_df = KOR_inc_wel_df.groupby('education_level')['income'].mean().sort_values()

plt.bar(edu_income_df.index, edu_income_df.values)
plt.title("income-education level")
plt.xlabel('education level')
plt.ylabel('education level')