# 2. 수집 데이터 전처리
- 데이터 Key값 변경
    - 데이터를 전치(Transpose)하여 Key값을 관측소 기준에서 날짜(Timestamp) 기준으로 변환 및 시계열 데이터 생성
- 대표 관측소 선정 (서울, 대전, 대구, 부산, 광주)
- 센서의 오작동, 고장, 사람의 실수 등으로 인해 발생한 결측을 선형 보간을 통해 대체

# 3. 기온 예측 모델 개발
- 사용 모델:
    - 신경망 계열: GRU, LSTM
    - 앙상블 계열: LightGBM, HistGradientBoost
- 학습 데이터 정의
    - 훈련 데이터 : 2017-01-01 00:00:00 ~ 2022-12-31 23:00:00 (5년)
    - 평가 데이터 : 2022-01-01 00:00:00 ~ 2022-06-30 23:00:00 (7개월)
    - 타겟 : 시간별 기온, 일별최저기온, 일별최고기온
- Input 변수 생성 및 평가 지표 정의
    - $X_{it} 부터 X_{it-4}$ 까지의 Lag 변수 생성 (기온, 풍량, 습도, 기압)
    - 평가지표 : mean absolute error(MAE)
- 모델 학습 결과
    - 각 Dimension (지역∩타겟) 에 해당하는 Best 모델 선정 및 시각화
 
[파일 설명]
1. df_accum.gzip: 20170101 ~ 20220701 기간 날씨 데이터
   (방법1) 검색창에 아래 google drive 링크 타고 들어가서 직접 파일 다운 
   - https://drive.google.com/file/d/14Vxtncy1A5wIwS6_GomRLApg14oKH-gv/view?usp=sharing

   (방법2) google colab에 개별 구글드라이브 연동 후, google_drive_downloader 라이브러리 통해 파일 다운
```
    from google.colab import drive
    import os
    
    drive.mount('/content/drive')
    
    os.chdir('{해당 경로 지정}')
    
    !ls


  # https://drive.google.com/file/d/14Vxtncy1A5wIwS6_GomRLApg14oKH-gv/view?usp=sharing
    from google_drive_downloader import GoogleDriveDownloader as gdd
    
    gdd.download_file_from_google_drive(file_id='14Vxtncy1A5wIwS6_GomRLApg14oKH-gv',
                                        dest_path='./df_accum.gzip',
                                        unzip=False)
```

2. awsId_awsNames.json: 관측소ID-관측소명 매핑 json 파일
3. model-result-test.csv: 모델 성능 결과 (MAE)
4. graph.zip: 관측소별, 타겟별, 모델별 (60개) 에 대한 시계열 그래프 
   
