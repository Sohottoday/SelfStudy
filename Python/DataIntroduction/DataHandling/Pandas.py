# Pandas 주요 구조
# 자료구조 : Series
# 1차원 데이터를 표현 : index
# pd.Series(['사과', '바나나', '딸기'])
# pd.Series(['사과', '바나나', '딸기'], index=[3,2,3])

# Series index 의 특성
# 키밸류 형식이지만 중복이 가능하고 순서개념이 있다.
# 음수 인덱스는 지원하지 않는다.

# 자료구조 : Dataframe
# 2차원 데이터를 표현
# 엑셀파일, csv파일, 데이터베이스 등으로부터의 생성 지원
# index : 행에서의 index
# Columns: 열에서의 index

# pd.read_  상태에서 tab을 누르면 다양한 형식 제공을 볼 수 있다.
# df = df.set_index('이름')   형식으로 행에 이름을 지정할 수 있다.
# df.loc['영희']
# df['수학']        # 이런식으로 보고싶은것만 볼 수도 있다.
# df['국어'] + df['수학']       이런식으로 사칙연산도 가능
# df['평균'] = (df['국어'] + df['수학'] + df['영어']) // 3      이런식으로 평균 컬럼을 만들어 바로 삽입 가능
# df.to_excel('data/score_result.xlsx')     이런식으로 엑섹 파일로 저장 가능
