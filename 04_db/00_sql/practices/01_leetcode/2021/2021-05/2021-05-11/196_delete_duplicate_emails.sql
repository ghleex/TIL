DELETE p1
FROM Person as p1, Person as p2
WHERE p1.Email=p2.Email AND p1.Id > p2.Id