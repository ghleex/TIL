SELECT ROUND(LAT_N, 4)
FROM (SELECT LAT_N, PERCENT_RANK() OVER (ORDER BY LAT_N) percent FROM STATION) a
WHERE percent = 0.5;
/*
PERCENT_RANK() 함수
특정값(수치)이 전체에서 몇 퍼센트인지 계산해주는 함수

이 문제에서는 PERCENT_RANK() 함수 결과 값이 0.5가 되는 경우 중앙값이라 할 수 있음
*/