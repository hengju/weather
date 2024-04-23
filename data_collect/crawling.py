url = f'https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?{timestamp}&-60&MINDB_60M&0&m&M'
print("URL: ", url)
response = requests.get(url)
# print(response.encoding)
# 인코딩된 ISO-8859-1에서 EUC-KR로 디코딩해주기
html = response.content.decode('EUC-KR')
