import requests
from bs4 import BeautifulSoup
import pandas as pd

# def fnguide_search(query):
#     url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode={query}"
#     print(url)
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         table = soup.find(id='highlight_D_A')
#         header = table.find_all('thead')[0].find_all('th')
#         header_text = [th.find('div').get_text() for th in header]
#         data = []
#         num_columns = len(header_text)
#         for row in table.find('tbody').find_all('tr'):
#             tmp = [cell.text.strip() for cell in row.find_all('td')]
#             if tmp[0] == 'IFRS(연결)':
#                 tmp = ['IFRS(연결) - ' + header_text[i] + tmp[i] for i in range(len(tmp))]
#             if len(tmp) != num_columns:
#                 tmp.extend([''] * (num_columns - len(tmp)))
#             data.append(tmp)
#         df = pd.DataFrame(data, columns=header_text)
#         df_transposed = df.transpose()
#         df_transposed.to_csv(f'{query}_output_transposed.csv', index=False)
#         print("전치된 CSV 파일이 성공적으로 저장되었습니다.")
#     else:
#         print("검색에 실패했습니다.")
#
# # 검색어 입력 받기
#
#
# # query = input("검색할 기업의 종목코드를 입력하세요: ")
# # fnguide_search(query)
#
# code_list = []
# with open('종목별 코드.csv', 'r', encoding='UTF8') as f:
#     data = f.readlines()
#     for i in data:
#         i = i.split(',')
#         code_list.append(i[0])
#
# print(code_list)
# print(len(code_list))
# print(code_list[1:-1])
#
# for i in code_list[:5]:
#     fnguide_search(i)
