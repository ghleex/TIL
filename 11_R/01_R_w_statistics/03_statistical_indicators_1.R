boxplot(c(1:10), horizontal=T)
boxplot(c(1:10, 20), horizontal=T)

boxplot.stats(c(1:10, 20))

set.seed(1234)
x <- sample(1:10, 6)
x
x_bar <- mean(x)
sum((x - x_bar)^2) / (length(x) - 1)
var(x); sd(x)
x <- rep(5, 10)
y <- c(1:10)
z <- c(3, 4, 5, 6, 7, 4, 5, 6, 5, 5)
hist(x, breaks=0:10)
hist(y, breaks=0:10)
hist(z, breaks=0:10)

sd(x); sd(y); sd(z)

mydata <- read.csv('https://www.theissaclee.com/ko/courses/rstat101/examscore.csv', header=TRUE)
var(mydata$midterm)
sd(mydata$midterm)
