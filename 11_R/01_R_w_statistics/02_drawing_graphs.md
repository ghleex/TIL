# R w/ Statistics

## 그래프 그리기 전에..

### 1. Dataframe 의 컬럼명으로 열에 접근하기

```R
> mydata$gender
 [1] "F" "M" "F" "M" "M" "M" "M" "M" "M" "M" "F"
[12] "F" "M" "M" "M" "F" "F" "F" "M" "M" "M" "M"
[23] "M" "M" "M" "M" "F" "F" "F" "M"
```



## 그래프 그리기

### 1. Pie Chart

* Categorical Data 다룰 때 사용
  * Gender: Male - Female
  * Dataframe 의 열 이름 바꾸기도 가능
  * F/M 을 여성/남성으로 바꾸기: `names(mytable) <- c('여성', '남성')`

```R
pie(
    mytable,
    main='학생 성별 분포'
)
```

![pie_1](https://user-images.githubusercontent.com/52685206/107211405-d6de1400-6a48-11eb-8767-c03d2eb355cd.png)

* 차트 내 원하는 좌표 위치에 문구를 삽입할 수 있음

  ```R
  # x축, y축 좌표, 넣을 문구
  text(0.3, 0.3, '33.3%')
  text(-0.3, -0.3, '66.7%')
  ```

  ![image](https://user-images.githubusercontent.com/52685206/107211964-9af77e80-6a49-11eb-8ce9-28d272757c4c.png)



-----

### 2. 줄기-잎 그래프(Stem and leaf plot)

```R
> stem(mydata$midterm)

  The decimal point is 1 digit(s) to the right of the |

  0 | 9
  1 | 5
  2 | 478899
  3 | 456889
  4 | 22366889
  5 | 01223
  6 | 35
  7 | 6
```

* `|`을 기준으로 십의 자리가 좌측에, 일의 자리가 우측에 옴

* 우측에 있는 숫자 하나씩을 좌측의 수와 연결하면 됨

  * 09, 15, 24, 27, ...  , 53, 63, 65, 76

* 단위를 변경하는 것도 가능: `scale`을 이용하며, 기본값은 1로 설정(10 단위)

* 아래는 `scale=2` (5 단위)인 경우

  ```R
  > stem(mydata$midterm, scale=2)
  
    The decimal point is 1 digit(s) to the right of the |
  
    0 | 9
    1 | 
    1 | 5
    2 | 4
    2 | 78899
    3 | 4
    3 | 56889
    4 | 223
    4 | 66889
    5 | 01223
    5 | 
    6 | 3
    6 | 5
    7 | 
    7 | 6
  ```

* 아래는 `scale=0.5` (20 단위)인 경우

  ```R
  > stem(mydata$midterm, scale=0.5)
  
    The decimal point is 1 digit(s) to the right of the |
  
    0 | 95
    2 | 478899456889
    4 | 2236688901223
    6 | 356
  ```



-----

### 3. 히스토그램(Histogram)

* 기본 형태

```R
hist(mydata$midterm)
```

![hist_1](https://user-images.githubusercontent.com/52685206/107214658-903ee880-6a4d-11eb-877c-6cc4f580c719.png)

* 단위 변경하기(`breaks` 이용)

  ```R
  hist(mydata$midterm, breaks=c(0, 20, 40, 60, 80))
  # 리사이클링 개념을 이용하여 표현 가능(`c(0:4) * 20` == [0, 20, 40, 60, 80])
  hist(mydata$midterm, breaks=c(0:4) * 20)
  ```

  ![hist_2](https://user-images.githubusercontent.com/52685206/107216072-8f0ebb00-6a4f-11eb-9e4a-f08cdc150c70.png)

* 그래프 제목과 축 제목도 넣을 수 있음

  ```R
  hist(
    mydata$midterm,
    breaks=c(0:16) * 5, # 구간에 알맞게 단위 설정 가능
    main='중간고사 분포',
    xlab='점수',
    ylab='빈도'
  )
  ```

  ![hist_3](https://user-images.githubusercontent.com/52685206/107216163-b36a9780-6a4f-11eb-8b0c-352c8deee4f7.png)



-----

### 4. 상자 그림(Box plot)

```R
boxplot(
  mydata$midterm,
  main='시험 점수 분포',
  xlab='점수',
  horizontal=T
)
```

![boxplot_1](https://user-images.githubusercontent.com/52685206/107217272-4952f200-6a51-11eb-942a-160347d12025.png)

* 여러 개를 띄우기도 가능

  ```R
  boxplot(
    mydata$midterm,
    mydata$final,
    main='시험 점수 분포',
    xlab='점수',
    ylab='시험 종류',
    # 개별 boxplot 이름 설정
    names=c('중간', '기말'),
    horizontal=T
  )
  ```

  ![boxplot_2](https://user-images.githubusercontent.com/52685206/107217386-70112880-6a51-11eb-96bc-00a71567d0a5.png)



-----

### 5. 산점도(Scatter plot)

```R
plot(
  mydata$midterm, mydata$final,
  xlab='중간고사',
  ylab='기말고사',
  main='시험점수 산점도',
  asp=1		# 가로/세로 비율을 일정하게 하려면 설정
)
```

![scatter](https://user-images.githubusercontent.com/52685206/107217533-a484e480-6a51-11eb-82e2-7ac48c70ebb9.png)