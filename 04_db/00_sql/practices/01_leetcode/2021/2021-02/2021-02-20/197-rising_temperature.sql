SELECT today.id
FROM Weather AS today
     INNER JOIN Weather AS yesterday ON DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY) = today.recordDate
WHERE today.temperature > yesterday.temperature