'''
 import seaborn as sns
 sns.함수(x=x열이름,y=y열이름,data=데이터셋) 
 sns.함수(x=데이터셋[열이름],y=데이터셋[열이])

 barplot : x의 y값들 평균
 boxplot: x의 y 사분위분포

 lineplot
 regplot:  x의 y의  선형 상관 관계(선) (x가 연속형 수열,시계열 ,hue 미지원)
 lmplot:  x의 y의  선형 상관 관계(선) (x가 이산형(범주형,hue 지원)):hue 옵션을 사용해서 카테고리별 비교가 가능

 scatterplot: x의 y의 스캐터 플롯(산점도)
 pairplot: 각 열의 값 조합의 스캐터 플롯
 countplot: x별 빈도수
 histplot
 distplot: x구간별 빈도수 분포 히스토그램,밀도함수
 '''
 
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

tips = sns.load_dataset("tips")#팁 데이터
tips.head()
tips.info()
tips.describe()

#%% barplot
# x별 y별
# 신뢰확률 95%
# 중심선(오차막대)은 신뢰구간을 의미
sns.barplot(x='day', y='total_bill',data=tips)
plt.title('요일별 전체 식사대금')

sns.barplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('요일별 성별 전체 식사대금')

sns.barplot(x='day', y='tip',data=tips)
plt.title('요일별 팁 금액')

sns.barplot(x='day', y='tip',data=tips, hue='sex')
plt.title('요일별 성별 팁 금액')

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
sns.barplot(x='day', y='total_bill',data=tips, hue='sex')
plt.title('요일별 성별 전체 식사대금')
ax1 = fig.add_subplot(2,1,2)
sns.barplot(x='day', y='tip',data=tips, hue='sex')
plt.title('요일별 성별 팁 금액')

import numpy as np
# estimator = 중간값, 오차막대=표준편차
sns.barplot(x='day',y='total_bill', data=tips,
            estimator=np.median,ci='sd')
plt.title('요일별 전체 식사대금')
# ci=None하면 오차막대 비출력
sns.barplot(x='day',y='total_bill', data=tips,
            estimator=np.median,ci=None)
plt.title('요일별 전체 식사대금')

#%% box(상자)plot
# IQR = Q3 - Q1
# 3사분위수와 1사분수의 차이(Q3-Q1)를 IQR(interquartile range)
# Q0 = 1사분위 수보다 1.5 x IQR만큼 낮은 값(ㅗ)
# Q4 = 3사분위 수보다 1.5 x IQR만큼 높은 값(T)
# 바깥의 다이아몬드점은 아웃라이어(outlier,이상값)

sns.boxplot(x="day", y="total_bill",data=tips)
plt.title("요일별 전체 식사대금")

plt.figure(figsize=(9,7))
sns.boxplot(x="day", y="total_bill",data=tips, hue='sex')
plt.title("요일별 성별 전체 식사대금")

plt.figure(figsize=(9,7))
sns.boxplot(x="day", y="total_bill",data=tips, hue='smoker')
plt.title("요일별 흡연여부별 전체 식사대금")


# 인원수별 팁금액 boxplot
#인원수 3 경우 : 팁금액이 매우 큰 금액(10)이 보이고
#2Q(중앙값) 조금 위쪽에 보인다
#인원수 4 경우 : 팁금액의 분포가 넓게 다양하게 보인다
plt.figure(figsize=(9,7))
sns.boxplot(x='size', y="tip",data=tips)
plt.title("인원수별 팁 금액")

#%% lineplot
# 평균값을 실선으로 95% 신뢰구간을 범위로 시각화
# x에 따른 y의 변동량(변화량)
# 데이터가 모두 연속적인 실수값이고 
sns.lineplot(x='day', y='total_bill',data=tips)
plt.title('요일별 전체 식사대금')

sns.lineplot(x='total_bill', y='tip',data=tips)
plt.title('식사대금에 따른 팁금액')

#인원수가 증가하면 팁 증가하는 추이
#인원수가 증가하면 팁의 분포범위(편차) 크다
#예 2인은 분포범위(편차) 일정하고 
#5인은 분포범위(편차) 크다 
sns.lineplot(x='size', y='tip',data=tips)
plt.title('인원수에 따른 팁금액의 변동')

#hue 그룹화
sns.lineplot(x='total_bill', y='tip',data=tips, hue='smoker')
plt.title('흡연여부별 식사대금에 따른 팁금액의 변동량')

#%%
'''
* 공분산 
평균을 중심으로 각 자료들이 어떻게 분포되어 있는지 
크기와 방향성을 나타낸다
편차의 변화량

x(설명,원인),y(결과)간의 관계성
cov(x,y) =  (x-x평균)(y-y평균)합의 평균

- 공분산 크기
의존(종속)성 정도 
공분산이 0 -> 비의존(종속) = 두 변수는 서로 독립적인 무관계

- 방향성 =공분산 부호
부호가 (+)인 경우는
X가 증가할 수록(X가 X평균보다 크면 ), Y도 증가(Y가 Y평균보다 크면 ),함(비례 관계  학습량과 기대성적)
부호가 (-)인 경우는
X가 증가할수록, Y는 감소함(반비례 관계 흡연량과 기대수명)
'A'열 데이터와 'B'열 데이터 간의 공분산을 산출하고자 할 경우 
df2["A"].cov(df2["B"])
'''
#---------------------------
'''
* 상관성
공분산에서 자료 분포의 방향성만 분리
공분산을 정규화
corr(x,y) = cov(x,y) /(x표준편차)(y표준편차) 
X와 Y가 있을 때, X의 증가 할 때 
Y가 감소하는지 증가하는지 정도를 측정

상관계수는 -1이상 +1이하의 값
절댓값이0.4 ~ 0.6 보통 관계이고 절댓값이 
0.6 이상이면 두 변수간에 관련성이 높다고 할 수 있다.
0에 가까우면 서로 관계가 없다는 것을 의미
df["A"].corr(df["B"]) 
※ 모든 열들 간의 상관계수
df.corr()

직급과 급여처럼 어느 한 변수가 다른 변수에 미치는 영향 등을 알고자 할때 이러한 상관 분석이 유용
'''

#---------------------------
#등고선 스타일
#면적이 좁으면 경사가 가파르고 두 열값간의 상관관계가 높다 
sns.kdeplot(x="total_bill", y="tip",data=tips)
plt.title("흡연여부별 식사대금에 따른 팁금액의 변동량")
#등고선 스타일
#sns.jointplot(x="total_bill", y="tip",data=tips, kind="kde")

