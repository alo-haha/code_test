#컴퓨터 내부 ip주소를 구하는 프로그램
#import socket
#in_addr = socket.gethostbyname(socket.gethostname())
#print("내부 ip주소는 ", in_addr)

#컴퓨터 내부 ip주소를 구하는 프로그램2
#컴퓨터 외부 ip주소를 구하는 프로그램
import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))
print("내부 ip주소는 ", in_addr.getsockname()[0])

req = requests.get("https://www.ipconfig.kr/")

match = re.search(

    r'(\d{1,3}(?:\.\d{1,3}){3})',

    req.text

)

if match:

    print("외부 IP 주소:", match.group(1))

else:

    print("IP 주소를 찾을 수 없습니다.")