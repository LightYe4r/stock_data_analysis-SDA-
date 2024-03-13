from bs4 import BeautifulSoup
import requests
import pandas as pd

# 크롤링할 웹 페이지 URL
url = 'http://comp.fnguide.com/'

# 웹 페이지 내용을 가져오기
response = requests.get(url)
html_content = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_content, 'html.parser')

# 데이터 추출
data = []
# 테이블의 ID를 사용하여 해당 테이블을 찾음
table = soup.find(id='highlight_D_Q')
header = table.find_all('thead')[0].find_all('th')
header_text = [th.find('div').get_text() for th in header]

# 각 행의 데이터 수 확인
num_columns = len(header_text)

# 목차를 자동으로 추가하도록 수정
for row in table.find('tbody').find_all('tr'):
    tmp = [cell.text.strip() for cell in row.find_all('td')]
    # 첫 번째 열이 'IFRS(연결)'인 경우에만 목차 추가
    if tmp[0] == 'IFRS(연결)':
        tmp = ['IFRS(연결) - ' + header_text[i] + tmp[i] for i in range(len(tmp))]
    # 각 행의 데이터 수가 헤더의 열 수와 다른 경우 빈 데이터를 추가하여 일치시킴
    if len(tmp) != num_columns:
        tmp.extend([''] * (num_columns - len(tmp)))
    data.append(tmp)

# DataFrame 생성
df = pd.DataFrame(data, columns=header_text)

# DataFrame 전치
df_transposed = df.transpose()

# CSV 파일로 저장
df_transposed.to_csv('output_transposed.csv', index=False)

print("전치된 CSV 파일이 성공적으로 저장되었습니다.")
