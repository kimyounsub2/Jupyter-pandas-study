import cx_Oracle as oci

# Oracle 서버와 연결(Connection 맺기) 
conn = oci.connect('system/manager@localhost:1521/xe')

# Oracle DB의 emp 테이블 검색(select)
cursor = conn.cursor() # cursor 객체 얻어오기
cursor

'''
파이썬 기반으로 입사일(HIREDATE)이 81년도인 사원의 모든 정보를 출력하라
(sql은 오라클의 substr 함수를 사용)
'''
sql = '''
select *
from emp
WHERE SUBSTR(HIREDATE, 1, 2) = '81'
'''
cursor.execute(sql)

for rs in cursor: # cursor에는 result(행) set(집합) 저장, 행적출
     print(rs)  # 행튜플 출력
     
rows = cursor.fetchall() # 모든 행을 가져올수 있다.
for rs in rows:
    print(rs)
conn.close()

#%% DtatFrame과 오라클
import pandas as pd
# read_sql(sql, 접속객체)
df=pd.read_sql('select * from emp', conn)
df.columns
df.shape
df.values
df.info()

df['ENAME']
df['SAL']
df['COMM']
df[df['SAL']>=3000]
df[df['DEPTNO'] ==20]

# 급여가 3000이상이면 '고액' 아니면 '저액'으로 분류
def sal_level(x):
    '''
    급여가 3000이상이면 '고액' 아니면 '저액'으로 분류
    Parameters
    ------
    x : float64
        급여.
        
    Returns
    ------
    res : TYPE 
          급여등급
    '''
    if x >= 3000:
        res='고액'
    else:
        res='저액'
    return res

help(sal_level)
# 열의 행값이 반복적으로(세로방향) sal_level()의 매개변수 x에 전달적용
type(df['SAL'].apply(sal_level)) # pandas.core.series.Series 시리즈 형식이기 떄문에 코딩이 가능하다
df['LVL'] = df['SAL'].apply(sal_level)
df

'''
모든 사원의 연봉을 계산하여 ANNSAL 컬럼을 만들어 
연봉을 입력하고 연봉이 30000 이상이면 'High' 아니면 'Low'을 가지는 GRD 컬럼을 추가한다.
단 연봉= SAL * 12 + COMM이고 if: else: 로 함수 정의하여 apply()를 활용
'''
file = pd.read_sql('select * from emp', conn)
# 데이터 전처리
file.info()
file['SAL']
file['COMM'] # null은 NaN이 있어 변환해줘야 한다.
# file['COMM']이 NaN포함되면 0계열 값으로 변환
file['COMM'].fillna(0,inplace=True)
file['COMM']
# 연봉계산
file['ANNSAL'] = file['SAL'] * 12 + file['COMM']
def sal_level1(x):
    if x >= 30000:
        res ='High'
    else:
        res = 'Low'
    return res
file['GRD'] = file['ANNSAL'].apply(sal_level1)
file

# 부서(dept) 테이블 데이터셋을 DataFrame으로 읽어서 사원 DataFrame과 내부조인한다.
sql = '''
SELECT d.deptname, e.ename FROM dept d INNER JOIN emp e ON e.deptno = d.deptno
'''
df = pd.read_sql('select * from emp', conn)
df2 = pd.read_sql('select *from dept',conn)
# pd.merge(df,df2, on='DEPTNO',how='inner') on,how를 생략하면 자연스럽게 조인을 찾아준다
pd.merge(df,df2)
conn.close()

# 사원 DataFrame의 복사본과 원본을 위,아래로 행 중복합치기
df = pd.read_sql('select * from emp', conn)
df2 = df.copy()
# axis=0이 적용되기 때문에 행방향(위아래)으로 데이터프레임을 이어붙인다.
# 열방향axis=1(좌우)
# 그냥 이어붙이니 행 인덱스번호도 그대로 가져왔기때문에, ignore_index=True을 줘서 인덱스를 재배열 할 수 있다.
df3 = pd.concat([df,df2], axis=0, ignore_index= True)   
df3

#%% DataFrame을 테이블로 지정
# sqlalchemy
from sqlalchemy import create_engine    

# Oracle 서버와 연결(Connection 맺기) 
conn = oci.connect('system','manager','localhost:1521/xe')

# 접속후 engine 생성
engine = create_engine('oracle+cx_oracle://system:manager@localhost:1521/xe')

# df_emp 테이블에 테이터를 저장
df.to_sql('df_tmp',
          engine,
          index=False) 
pd.read_sql_query('select * from df_tmp', engine)
