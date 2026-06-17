from currency_converter import CurrencyConverter # currency_converter 모듈에서 CurrencyConverter 클래스 가져오기
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip') # 유로 환율 데이터 사용
print(cc.convert(100, 'JPY', 'KRW')) # 1 엔을 원화로 환산
