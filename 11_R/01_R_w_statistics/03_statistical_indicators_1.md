# 데이터를 요약하는 통계 지표 1

## 1. 평균값과 중앙값

### 평균값

![image](https://user-images.githubusercontent.com/52685206/108709718-707fe800-7556-11eb-8c71-0a3c8c8a69c9.png)

* 구하는 공식
  $$
  {\bar{x}} = \frac{\sum\limits_{i=1}^{n}{x}}{n}
  $$
  

![image](https://user-images.githubusercontent.com/52685206/108709842-9a390f00-7556-11eb-83bf-3b867d8b48cd.png)

### 중앙값

* 데이터가 순서대로 정렬되어 있어야 함. 그렇지 않다면 sorting부터 해야 함

* Skewness

  |  Skew to the right   |        대칭 분포         |  Skew to the left  |
  | :------------------: | :----------------------: | :----------------: |
  | 오른쪽으로 기운 분포 | Symmetrical Distribution | 왼쪽으로 기운 분포 |
  |    평균 != 중앙값    |      평균 = 중앙값       |   평균 != 중앙값   |

  ![Relationship_between_mean_and_median_under_different_skewness](https://user-images.githubusercontent.com/52685206/108710918-05371580-7558-11eb-8254-424f545f04c7.png)

* 구하는 공식

  * 전체 데이터 개수가 홀수인 경우
    $$
    x_{(\frac{n+1}{2})}
    $$

  * 전체 데이터 개수가 짝수인 경우
    $$
    \frac{x_{(\frac{n+1}{2})}+x_{(\frac{n+2}{2})}}{2}
    $$



### 평균과 중앙값의 특성

* 평균이 중앙값보다 극단 값이 민감함

  데이터가 다음과 같이 [  1  2  3  4  (5  |  50)  ] 있다고 한다면

  괄호 안의 수가 5인 경우

  * 평균: 3, 중앙값: 3

  괄호 안의 수가 50인 경우

  * 평균: 12, 중앙값: 3

* 극단값이 바뀜에 따라 평균이 영향을 더 많이 받음을 확인할 수 있다.