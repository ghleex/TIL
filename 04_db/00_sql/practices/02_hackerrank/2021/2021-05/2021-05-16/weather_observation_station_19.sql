/* 
The Euclidean Distance
sqrt((a - b)^2 + (c - d)^2)
*/
SELECT 
    ROUND(SQRT(POW(ABS(MIN(LAT_N) - MAX(LAT_N)), 2) 
               + POW(ABS(MIN(LONG_W) - MAX(LONG_W)), 2)), 4)
FROM STATION;