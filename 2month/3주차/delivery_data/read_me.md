- 데이터 전처리와 속성 생성
    1. created_at과 actual_delivery_time에 대해 datetiime 형식 열로 변환
    2. 모델의 예측력에 영향을 받지 않기 위해 estimated_store_to_consumer_driving_duration', 'estimated_order_place_duration' 열 삭제
    3. 나머지 열들의 결측치가 전체 데이터에 비해 많지 않으므로 결측치가 존재하는 행 삭제
    4. datetime 열들을 사용해 소요 시간(초), total_time 열 생성
    6. describe()로 살펴본 이상치와 존재할 수 없는 값들(소요 시간이 - 인 것 등) 삭제
    7. 배달하는 시간대와 요일이 중요할 것이라 생각해 해당 열들 생성
    8. 범주형으로 존재하는 store_primary_category열 LabelEncoder 사용해 변환


- 사용 모델과 기법

    사용 모델은 시간과 효율성면에서 우수한 Gradient Boosting model인 Xgboost 사용, 이 때 GridSearchCv와 paramGrid를 사용해 최적의 파라미터를 찾을 수 있게 함, 손실 함수는 sklearn에서 제공하는 neg_mean_squared_error를 사용

- 최종 평가지표
    
    rmse =  890.0616056394979
    under_prediction_ratio = 0.42881555686505596