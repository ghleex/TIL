mydata <- read.csv('https://www.theissaclee.com/ko/courses/rstat101/examscore.csv', header=TRUE)
head(mydata)

mydata[, 3]

# '$' 기호 사용
# dataframe의 컬럼명으로 열에 접근
mydata$gender

# pie chart
# categorical data
# example: gender - male / female
mytable <- table(mydata$gender)
mytable

names(mytable) <- c('여성', '남성')
mytable

pie(
  mytable,
  main='학생 성별 분포'
)

sum(mytable)
c(10, 20) / 30

# x축, y축 좌표, 넣을 문구
text(0.3, 0.3, '33.3%')
text(-0.3, -0.3, '66.7%')


# 줄기-잎 그래프(Stem and leaf plot)
stem(mydata$midterm)
# 단위 변경: scale(2를 쓰면 5단위로 쪼갬)
stem(mydata$midterm, scale=2)
# 0.5를 쓰면 20단위로 나뉨
stem(mydata$midterm, scale=0.5)


# 히스토그램(Histogram)
hist(mydata$midterm)
# 단위 변경
hist(mydata$midterm, breaks=c(0, 20, 40, 60, 80))
hist(mydata$midterm, breaks=c(0:4) * 20)
hist(
  mydata$midterm,
  breaks=c(0:16) * 5,
  main='중간고사 분포',
  xlab='점수',
  ylab='빈도'
)


# 상자 그림(Box plot)
boxplot(
  mydata$midterm,
  main='시험 점수 분포',
  xlab='점수',
  horizontal=T
)

mydata$midterm[1] <- 100 # Outliers
mydata$midterm

boxplot(
  mydata$midterm,
  mydata$final,
  main='시험 점수 분포',
  xlab='점수',
  ylab='시험 종류',
  # 개별 boxplot 이름
  names=c('중간', '기말'),
  horizontal=T
)


# 산점도(Scatter plot)
plot(
  mydata$midterm, mydata$final,
  xlab='중간고사',
  ylab='기말고사',
  main='시험점수 산점도',
  asp=1
)
