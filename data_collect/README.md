## [데이터 요약 및 데이터 수집 배경]
### A. 지상-방재기상관측(AWS)
- 데이터 관측 주기: 시간별
- 방재기상관측이란 지진 · 태풍 · 홍수 · 가뭄 등 기상현상에 따른 자연재해를 막기 위해 실시하는 지상관측을 말함
- 관측 공백 해소 및 국지적인 기상 현상을 파악하기 위하여 전국 약 510여 지점에 자동기상관측장비(AWS)를 설치하여 자동으로 관측
- 기상청 날씨누리 사이트에서 해당 데이터와 관련있는 URL을 가져와 반복문을 통해 크롤링 (AWS는 공공기관외 일반 사용자에게 시간별 AWS API를 따로 제공하지 않음)
> 시간별 : https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?{%Y%m%d%H%S}&-60&MINDB_60M&0&m&M

**[참고]**
- AWS(Automatic Weather System) 관측소가 다른 기상장비에 비해서 전국적으로 많이 퍼져있고 큰 도시뿐만 아니라 도서산간지역까지 다 커버함
- 시군구 단위로 데이터를 제공하며 데이터가 기상청에서 제공하는 다른 데이터보다 더 풍부함  (AWS는 약 500개 관측소, ASOS는 약 100개 관측소)

## [데이터 상세 설명]
## 1. AWS
#### A. 시간별 (Hourly)
- 기상청 AWS (지상-방재기상관측) 시간별 데이터
- 대한민국 시간 기준으로 최신 1시간마다 업데이트 되는 데이터를 수집
- 비동기적 크롤링
- 원천 사이트인 기상청 날씨누리 > 육상 > 지역별상세관측자료(AWS)
  > (https://www.weather.go.kr/plus/land/current/aws_table_popup.jsp)
- 위 원천 사이트에서  기상청 서버에서 표 데이터를 렌더링하는 URL 추출
- https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?{%Y%m%d%H%S}&-60&MINDB_60M&0&m&M
- 실제 기상변화 관측시간과 발표시간 1시간 차이남
- 데이터를 받아오는 URL의 timestamp 파라미터는 발표시간 기준임 (실제 데이터 관측시각보다 1시간이 늦음)
- URL에 들어가는 timestamp 파라미터가 22/07/01 00:00일 경우, 실제 데이터는 22/06/30 23:00에 해당

**a. 대한민국 시간 기준으로 현재 시간 (timestamp) 지정**
- 데이터를 받아오는 URL의 timestamp 파라미터는 발표시간 기준임 (실제 데이터 관측시각보다 1시간이 늦음)
- 따라서, datetime.datetime.now()에 1시간을 더해줌

**b. 사이트 접속 및 request를 통해 데이터 요청**
> https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?{%Y%m%d%H%S}&-60&MINDB_60M&0&m&M
* for문을 통해 %Y%m%d%H%00 형식인 timestamp를 바꿔가며 해당 URL 접속
* request를 통해 데이터 요청

**c. BeautifulSoup로 html 정보에서 필요 데이터 파싱**

**d. 최종 결과 CSV/GZIP파일로 저장**
