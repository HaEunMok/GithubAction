import requests
from bs4 import BeautifulSoup

# 리디 북스에서 text를 받아오기
url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

# 텍스트 파싱 
soup = BeautifulSoup(html, 'html.parser')

# 제목을 넘버링하여 보여주기
bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
