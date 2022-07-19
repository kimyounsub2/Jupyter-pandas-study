#%% 서브플롯
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')

# 사인과 코사인 곡선 시각화
# x: 0 ~ 360도 등간격 배열
x = np.linspace(0,360,360)
x2 = np.linspace(0,360,360)

# y
y = np.sin(np.deg2rad(x))
y2 = np.cos(np.deg2rad(x2))

# 음수부호 보이기
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 가로,세로크기 인치
fig = plt.figure(figsize=(5,10))

# 전체플롯(창 = 피규어)의 figure 제목
fig.suptitle('사인과 코사인 곡선')

# 방법1. figure.add_subplot()으로 복수 사인 subplot 생성
ax = fig.add_subplot(2,1,1)
# subplot 그리기
ax.plot(x,y)

# 코사인 subplot 생성
ax2 = fig.add_subplot(2,1,2)
# subplot 그리기
ax2.plot(x2,y2)

####
fig = plt.figure(figsize=(5,10))
# 방법2. plt.subplot()으로 복수개의 
plt.subplot(2,1,1)# plt.subplot
# subplot 그리기
plt.plot(x,y)
plt.title('사인')

# 코사인 subplot 생성
plt.subplot(2,1,2)
# subplot 그리기
plt.plot(x2,y2)
plt.title('코사인')

#%% 히스토 그램
import numpy as np
y = np.random.randn(50)
plt.hist(y,bins=10)
plt.hist(y,bins=5)
# 도수 = 확률밀도
# 막대의 아래 면적이 1이 정규화
plt.hist(y,bins=20, density=True)

#%% 히트맵
# 색상을 이용해서 시각화
# 표준정규분포를 갖는 2차배열
y = np.random.randn(50).reshape(5,10)
plt.matshow(y) # 히트맵
plt.colorbar() # 칼라바(값들의 색생범위)

#%% df의 함수 사용
import pandas as pd
df = pd.DataFrame(np.random.rand(10,4), 
                  columns = ['A','B','C','D'], 
                  index = np.arange(0,100,10))
df

# 라인플롯
plt.plot(df)
df.plot() ## 범례 함께 표시
# 열 라인 플롯
df['B'].plot()
# 특정한 열간의 라인 플롯
# df.plot(x='A',y='B')
df.plot('A','B')

# 바플롯
df.plot(kind='bar') ##범례 함께
# df.plot.bar()
df.plot('A','B', kind='bar')

# 산점도 플롯
# df.plot.scatter('A','B')
df.plot('A','B',kind = 'scatter')

#%% 면적(area)그래프
# 선 그래프 -> 면그래프
# 두 개 이상의 데이터들의 트렌드와
# freq = 'M' 이면 index = 1월에서 6월
# freq = 'D' 이면 index = 1일에서 6일로 본다
df = pd.DataFrame({
   '판매자수': [3, 2, 3, 9, 10, 6],
   '구매자수': [5, 5, 6, 12, 14, 13]   
}, index=pd.date_range(start='2020/01/01', 
                       periods = 6,  freq='M'))
df = pd.DataFrame({
   '판매자수': [3, 2, 3, 9, 10, 6],
   '구매자수': [5, 5, 6, 12, 14, 13]   
}, index=pd.date_range(start='2020/01/01', 
                       end = '2020/07/01',  freq='M'))
df.plot.area()

#%% 퀴즈
'''
리스트들을 사전구조로 구성한 후 DataFrame으로 생성
학생명을  DataFrame 행인덱스로 설정
각 점수열마다 열의 큰값으로 나누는 정규화 작업 후 
학생의 평균점수를 출력하고 시각화한다.
'''
 
#plt.tight_layout() #서브플롯을 적절히 자동 배치 

x = ['안지영', '홍지수', '황예린']
y1 = [90, 85, 88] #국어
y2 = [85, 88, 90] #영어
y3 = [85, 97, 78] #수학

# 자료
# 리스트들을 사전구조로 구성한 후 DataFrame으로 생성 학생명을  DataFrame 행인덱스로 설정
df = pd.DataFrame({'국어': y1,'영어':y2,'수학':y3}, index = x)
df

# 기능
# 각 점수열마다 열의 큰값으로 나누는 정규화 작업 후
# 열 정규화 함수
# 변수를 담아 함수만들기
def norm(col,mx): # 점수열
    return col/mx

def norm2(col): # 점수열
    return col/np.max(col)

# 학생행 평균함수
def avg(row): # 학생행
    # np.집계함수(배열)
    # 배열.집계함수()
    return row.mean()

# 함수 호출
df = df.apply(lambda col:norm(col,np.max(col)), axis=0)
df = df.apply(norm2,axis=0)
df['평균'] = df.apply(avg, axis=1)
df

# 평균은 정규화된 값이므로 별도의 서브 플롯으로 처리
def show():
    plt.figure(figsize=(10,5)) # 윈도우창 크기인치
    plt.subplot(211) # 2행1열1번 행수열수순번
    plt.plot(df['국어'], 'ro-',label='국어')
    plt.plot(df['영어'], 'go-',label='영어')
    plt.plot(df['수학'], 'yo-',label='수학')
    plt.legend()
    plt.title('점수')

    plt.subplot(212)
    plt.bar(df.index, df['평균'],width=0.5)
    plt.title('평균')

    plt.tight_layout()
    
show()

#%%
# df의 함수 사용 
df.plot() 
df[["국어",'영어',"수학"]].plot()
df['평균'].plot(kind='bar',rot=0)

# 평균 상위 1개 추출
df_rank = df.sort_values(by ='평균',ascending=False)
df_rank.iloc[0,:]
df_rank.loc['홍지수']
df_rank.head(1)

#%% 퀴즈
'''
1. 전체 총인구수,총세대수,남자총인구수,여자총인구수 출력한다. 
2. 서울,부산, 대구, 인천, 광주, 대전지역의 총인구수와 세대수를 막대플롯한다. 
컬럼.str(문자열접근자)
컬럼.replace('찾을문자열','변경할문자열')
'''
file = pd.read_csv('C:/Users/A/Desktop/youn/python_day4/data/population_2020.csv')
file.columns
file.values
file.info()
#1
pd = file.loc[['행정구역','2020년02월_총인구수','2020년02월_세대수','2020년02월_남자 인구수','2020년02월_여자 인구수']]

#2
file = file.iloc[:6,:3]
file
file['행정구역'] = file['행정구역'].str[:5]
file
file['총인구수'] = file['2020년02월_총인구수'].str.replace(',','').astype('int')
file['세대수'] = file['2020년02월_세대수'].str.replace(',','').astype('int')
file1 = pd.pivot_table(data = file , index=['행정구역'] ,values=['총인구수','세대수']  )
file1
file1.plot.bar(rot=0)
#################

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
# CSV 파일을 읽어 들여 frame에 저장후 정제  
frame = pd.read_csv('C:/Users/A/Desktop/youn/python_day4/data/population_2020.csv', encoding="utf-8")    
#1, 2, 4, 5 열의 ','와 공백문자를 제거 후 정수 형변환
#컬럼이름이 한글이고 조금 복잡 ->  컬럼이름 간소화 정제 loc[] 산출
frame.columns=['지역', '총인구수', '세대수', '세대당_인구', '남자_인구수', '여자_인구수', '남여_비율']

frame.loc[:, ['총인구수', '세대수', '남자_인구수', '여자_인구수']] 
frame.loc[:,'총인구수']=frame.loc[:,'총인구수'].str.replace(',', '').replace(' ', '').astype('int64')
frame.loc[:,'세대수']=frame.loc[:,'세대수'].str.replace(',', '').replace(' ', '').astype('int64')
frame.loc[:,'남자_인구수']=frame.loc[:,'남자_인구수'].str.replace(',', '').replace(' ', '').astype('int64')
frame.loc[:,'여자_인구수']=frame.loc[:,'여자_인구수'].str.replace(',', '').replace(' ', '').astype('int64')
frame2 = frame.loc[:, ['총인구수', '세대수', '남자_인구수', '여자_인구수']]
frame2       
# sum() 메소드로 행 방향으로 합계를 구함
sum = frame2.sum(axis=0)
sum
# 1번
#출력화면
print('-' * 50)
print('국내 전체 인구 통계')
print('-' * 50)
print('- 총 인구수 : %d명' % sum.iloc[0])
print('- 총 세대수 : %d명' % sum.iloc[1])
print('- 총 남자 인구수 : %d명' % sum.iloc[2])
print('- 총 여자 인구수 : %d명' % sum.iloc[3])
print('-' * 50)

# 2번
from matplotlib import rc
rc('font', family='Malgun Gothic')

index = ['서울', '부산', '대구', '인천', '광주', '대전']
index
#'서울', '부산', '대구', '인천', '광주', '대전' 행의 총인구수
x1 = frame.iloc[:6, 1]
x1
#'서울', '부산', '대구', '인천', '광주', '대전' 행의 세대수
x2 = frame.iloc[:6, 2]
x2

# 두 시리즈로 합칠때 x1,x2 하나의 데이터프레임으로 합치기 : 예제1
df = pd.concat([x1,x2],axis=1,ignore_index=True) # 일반적으로 concat을 많이 활용한다.
df.index = index
df.columns=['총인구수','세대수']
x1.append(x2, ignore_index=True) # append함수는 위아래로 합쳐진다.
x1.join(x2, ignore_index=True) # 가로로 합쳐지기 위해서는 join함수를 사용하지만 Serise는 지원이 안된다

# 두 시리즈로 합칠때 x1,x2 하나의 데이터프레임으로 합치기 : 예제2
x1_lst = x1.values.tolist() #  x1.values 가능
x2_lst = x2.values.tolist() #  x2.values 가능
df = pd.DataFrame({'총인구수':x1_lst, '세대수':x2_lst}, index=index)
df

# 두 시리즈 x1, x2를 DataFrame변환후 하나의 DataFrame으로 합치기
test = x1.to_frame().append(pd.DataFrame(x2),ignore_index=True)
test.fillna(0)
test.dropna()
#1e7 지수 표기법
df.plot.bar(rot=0) 

#1e7 지수 표기법을 plain(십진수) 수정
plt.ticklabel_format(style = 'plain')
#gca() : 현재 Axes 객체 리턴
df.plot.bar(rot=0 ,ax=plt.gca()) 
