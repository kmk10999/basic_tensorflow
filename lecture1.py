import pandas as pd
lemon_direc = 'C:\\Users\\Myungsung\\Desktop\\딥러닝 공부\\Lecture1\\lemonade.csv' #파일 디렉토리
boston_direc = 'C:\\Users\\Myungsung\\Desktop\\딥러닝 공부\\Lecture1\\boston.csv' #파일 디렉토리
iris_direc = 'C:\\Users\\Myungsung\\Desktop\\딥러닝 공부\\Lecture1\\iris.csv' #파일 디렉토리

lemon_data = pd.read_csv(lemon_direc) #해당 디렉토리의 파일 data 불러오기
boston_data = pd.read_csv(boston_direc) #해당 디렉토리의 파일 data 불러오기
iris_data = pd.read_csv(iris_direc) #해당 디렉토리의 파일 data 불러오기





#data shape 출력, 맨위의 row는 변수들이므로 이를 제외한 data shape 출력
print(lemon_data.shape)
print(boston_data.shape)
print(iris_data.shape)

#column name 출력
print('레몬에이드 ', lemon_data.columns)
print('보스턴 ', boston_data.columns)
print('아이리스 ', iris_data.columns)

#독립변수, 종속변수 분리
lemon_dependent = lemon_data[['온도']] #독립변수 : Column Vector 이름
lemon_independent = lemon_data[['판매량']] #독립변수로 인한 종속변수 : Column Vector 이름
lemon_all_data = lemon_data[['온도', '판매량']] #data내의 모든 element

boston_dependent = boston_data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat']]
boston_independent = boston_data[['medv']]

iris_dependent = iris_data[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
iris_independent = iris_data[['품종']]

print(lemon_dependent.shape, lemon_independent.shape)
print(boston_dependent.shape, boston_independent.shape)
print(iris_dependent.shape, iris_independent.shape)