SELECT Employee.Name AS Employee
FROM Employee
     INNER JOIN Employee as Manager ON Employee.ManagerId = Manager.Id
WHERE Employee.Salary > Manager.Salary