# pyHadoop-k-means

I implemented a k-means algorithm that can be driven in a distributed processing environment. Enter distributed data and 'ceontroid.csv' in the mapper to calculate which cluster each data point belongs to. The reducer receives the result and calculates a new crontroid and modifies 'ceontroid.csv'.

분산처리 환경에서 구동할 수 있는 k-means 알고리즘을 구현하였다. mapper에 분산된 데이터와 'ceontroid.csv'를 입력하면 각 데이터 포인트가 어느 클러스터에 속하는지 계산한다. reducer는 그 결과를 받아 새로운 무게중심을 계산하고 'ceontroid.csv'를 수정한다. 
