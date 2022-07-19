#%% matplotlib
import matplotlib.pyplot as plt

# 세명 학생의 영어 성적 리스트
y = [20,30,40]
x = [1,2,3]

# 선 그래프
# plot(x,y)
plt.plot(x,y)

y=[85,88,90]
x=['kim','lee','kang']
plt.plot(x,y)

# 제목
plt.title('English Score of three Students')
# 축레이블
plt.xlabel('Student Name')
plt.ylabel('Score')

#%% 한글 시각화
#플롯 한글 깨짐 방지
plt.rc('font',family='Malgun Gothic')
#음수부호 보이기
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
# 글꼴 크기
matplotlib.rcParams['font.size'] = 16
y = [85,88,90]
x=['안지영','홍지수','황예린']
plt.plot(x,y)

# fontdict : 폰트 스타일 사전
plt.title('세명 학생의 영어 성적', fontdict={'size':18,'color':'green',
                                    'weight':'bold'})
plt.xlabel('이름')
plt.ylabel('성적')

#%% 키워드 args
def print_kwargs(**kwargs):
     print(kwargs)

member={
 "name":'foo',
 "age":3
}

# **로 언팩킹  
print_kwargs(**member)
#%% 한글시각화2
# 기본 폰트 Malgun Gothic, 크기 12
font = {'family' : 'Malgun Gothic',
        'size' : 12}

# 플롯 한글 깨짐 방지
plt.rc('font',**font)
y = [85,88,90]
x=['안지영','홍지수','황예린']
plt.plot(x,y)

# fontdict : 폰트 스타일 사전
plt.title('세명 학생의 영어 성적')
plt.xlabel('이름')
plt.ylabel('성적')

#%% 여러 개의 그래프를 범례(legend)와 함께 한 개의 으로 그리기

x = ['안지영', '홍지수', '황예린']
y1 = [90, 85, 88] #국어
y2 = [85, 88, 90] #영어
y3 = [85, 97, 78] #수학

#플롯 한글 깨짐방지 
plt.rc('font', family='Malgun Gothic') 
#플롯(axes)의 배경색 노랑 지정 
plt.rcParams['axes.facecolor'] = 'yellow'

#plt.plot(x,y1,c='red')
#plt.plot(x,y2,c='green')

#linestyle=':'점선 ,-- 파선 - 실선
#marker=d:다이아몬드
plt.plot(x,y1,c='red',linestyle='-', marker='o') 
# plt.plot(x,y2,c='green',linestyle='--', marker='x')
#style 값들을 하나의 문자열로 지정
plt.plot(x,y2,'g--x')
plt.plot(x,y3,'g:x')

# 범례 label과 위치
plt.legend(['국어','영어','수학'])
plt.title('세명 학생의 영어 성적', fontdict={'size':18,'color':'green',
                                    'weight':'bold'})
plt.xlabel('이름')
plt.ylabel('성적')
#%% bar(막대)플롯
# x 데이터가 카테고리 값인 경우
# 카테고리 별 y값의 크기 비교
plt.bar(['안지영', '홍지수', '황예린'], [85, 88, 90])
plt.barh(['안지영', '홍지수', '황예린'], [85, 88, 90])
plt.title('세명 학생의 성적',
          fontdict={'size':18,'color':'green'})
plt.xlabel('이름')
plt.ylabel('성적')

plt.bar(['안지영', '홍지수', '황예린'], [85, 88, 90], width=0.5, color='green')

#%% scatter(산점,산포) 플롯
# x,y의 상관관계 분포
plt.scatter(['안지영', '홍지수', '황예린'], [85, 88, 90])

y = [5,3,7,10,9,5,3.5,8]
x = range(len(y))
plt.scatter(x,y)

# 상관관계(비례) 보인다 y=2x
x = [1,2,3,4]
y = [2 * i for i in x]
plt.scatter(x,y)

#%% 축의 범위, 눈금값 지정
x = [1,2,3,4]
y = [2 * i for i in x]
plt.plot(x,y)

# 축의 범위 지정하여 변경
plt.xlim(0,10)
plt.ylim(0,20)

# 요소의 위치(눈금 = tick)
# 0부터 10까지 1씩 증가하는 눈금값
plt.xticks(range(0,11)) # 0부터1
plt.yticks(range(0,21,2))
# 그리드 표시
plt.grid(True)

#%% pie
labels = ['개구리','돼지','개','고양이']
sizes=[5,20,40,35]
colors = ['yellowgreen', 'gold', 'lightskyblue', 
          'lightcoral']
#돼지파이조각을 다른요소와 0.1 간격주어서 튀어나오게 한다
#explode = (0, 0.1, 0, 0) 
plt.title("반려동물 Pie Chart")
#startangle 90 :그래프의 시작 12시에서 반시계방향 요소 표시 개구리,돼지 이런순서
#autopct='%1.1f%%' : 요소값 소수점이하 1자리수 
#plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=90) 

plt.pie(sizes,labels=labels, colors=colors,
        autopct='%1.1f%%',startangle=90) 

#%%
import pandas as pd

x = ['안지영', '홍지수', '황예린']
y = [85, 88, 90]

df = pd.DataFrame(data=y, 
                  index=x,
                  columns=["성적"])
df
#각각의 리스트를 열로 간주하여 열들을 사전으로 묶음
data =  {"학생이름": x, "성적": y}
#사전을 DataFrame 변환
df = pd.DataFrame(data)
df
# plot(열,열)
plt.plot(df['학생이름'],df['성적'])
plt.plot(df.index, df['성적'])
# x가 생략되면 index가 x축
plt.plot(df['성적'])

# 파일저장
# 위 코드와 함께 한꺼번에 실행
plt.savefig('score.png')
#%% 퀴즈
'''
1. iris 데이터셋의  sepal_width 컬럼을 라인플롯한다.
2. iris 데이터셋의  sepal_width 컬럼을 산포플롯한다.
3. iris 데이터셋의  꽃 품종이름 별로 sepal_width 컬럼의 평균을 바플롯한다.
4. stock.png 참조하여 파이플롯한다.
'''
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('C:/Users/A/Desktop/youn/python_day4/data/iris.csv')
file.columns
file.values
file.info
file.head()
#1
sw = file['sepal_width']
plt.plot(sw) 

#########
plt.rc('font', family='Malgun Gothic') 
# 1. iris 데이터셋의  sepal_width 컬럼을 라인플롯한다.
plt.plot(file.index, file['sepal_width'])
plt.xlabel('행번호')
plt.ylabel('꽃받침의 두께')

#2
x = range(len(sw))
plt.scatter(x,sw)
#######
# 2. iris 데이터셋의  sepal_width 컬럼을 산포플롯한다.
plt.scatter(file.index, file['sepal_width'])
plt.xlabel('행번호')
plt.ylabel('꽃받침의 두께')

#3
kind = file.groupby(['species'], as_index=False).mean()
kind
ks=kind['species']
kw =kind['sepal_width']
plt.bar(ks,kw)
plt.title('꽃 품종이름 별 sepal_width 컬럼의 평균')
plt.xlabel('꽃종류')
plt.ylabel('평균')
#######
# 3. iris 데이터셋의  꽃 품종이름 별로 
# sepal_width 컬럼의 평균을 바플롯한다.
avg=file.groupby(by='species')['sepal_width'].mean()
type(avg)#Series
plt.bar(avg.index,avg)
plt.xlabel('품종')
plt.ylabel('꽃받침 두께의 평균')

#4
labels = ['삼성전자','현대차','포스코','네이버','카카오']
sizes=[50,20,10,10,10]
colors = ['yellow','green', 'pink', 'blue', 'red']
plt.title("stock.png 참조")
plt.pie(sizes,labels=labels, colors=colors,
        autopct='%1.1f%%',startangle=90,explode=[0, 0.1,0,0,0])
#######
# 4. stock.png 참조하여 파이플롯한다.
sizes=[50,20,10,10,10]
colors=['yellow','yellowgreen','pink','skyblue','red']
explode=(0,0.1,0,0,0)
labels=['삼성전자','현대차','포스코','네이버','카카오',]
plt.pie(sizes,colors=colors,explode=explode,
        labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
#파일저장
plt.savefig('stock.png')#위 코드와 함께 실행