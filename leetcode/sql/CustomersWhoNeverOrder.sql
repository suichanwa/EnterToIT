SELECT name as Customers
FROM Customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customerId
    FROM Orders
);
