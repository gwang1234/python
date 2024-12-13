import numpy as np
import pandas as pd

# score = pd.Series([95, 90, 85, 80, 75])
# print(score)

# arr = np.arange(12).reshape(4,3)
# print(arr)
# df = pd.DataFrame(arr)
# print(df)

# # 딕셔너리로 데이터프레임 생성
# df = pd.DataFrame({'name':['장은실','오경선','양숙희'],
#                     'score':[90,80,95],
#                     'dept':['com','eng','math']})
# print(df)


# filename='weather.csv'
# df = pd.read_csv(filename)
# print(df)

# df.shape
# df.info
# df.describe() 
# #기온(temp) 컬럼의 평균 출력하기
# print(df['temp'].mean())
# df.sort_values(by='max_wind')


# bank=pd.read_csv('bank.csv')
# bank['job'].value_counts() # job 열의 고유값 개수
# # bank['job'].value_counts(ascending=True) # 오름차순 정렬 

# bank['job'].unique() # job 열의 고유값 출력


dust=pd.read_excel('dust1.xlsx')
print(dust.info()) 
print(dust.head())

