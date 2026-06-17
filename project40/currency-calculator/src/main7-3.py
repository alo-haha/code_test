import requests # 환율 정보를 가져오기 위해 requests 라이브러리를 사용합니다.
from bs4 import BeautifulSoup # HTML 파싱을 위해 BeautifulSoup 라이브러리를 사용합니다.

def get_exchange_rate():
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    exchange_rates = {}
    for item in soup.select('.exchangeList